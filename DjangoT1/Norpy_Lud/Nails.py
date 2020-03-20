
class Material:
    """
        G: Material density
        Thick: Material thickness relative to the connection, mm
        Type: panel grade (CSP), Engineer wood product CLT or SPF construction
        lumber
    """
    def __init__ (self, G, Thick, Type):
        self.G = G
        self.Thick = Thick
        self.Type = Type

class Nail:
    """
        Dia: nail diameter, mm
        Len: nail length, mm
    """
    def __init__ (self, Dia, Len):
        self.Dia = Dia
        self.Len = Len


class O86_14_2017:
    """Based on O86-14 update 2 section 12.9 : Nails and spikes"""


    def __init__(self, J_E, J_A, J_B, J_D, material_1, material_2, Nail,
                 KD=1, KSF=1, KT=1, **kwarg):
        """
            Scope:
                Function to evaluate the lateral shear resistance of a nail
                fastener.
                Standard: section 12.9, Nails and spikes from CSA O86-14
                The resistance values specified in Clause 12.9 apply only to
                common round steel wire nails and spikes
                and common spiral nails spiraled to head as defined in
                CSA B111.
        
                Validation for minimum dimensions integrated in t1, t2 and f1.
                (See CSA O86-14, Figure 12.9.2.2)
            
            Constant:
                nf: number of fastener (constance = 1)

            Arguments:
                ns: Shear planes (1 or 2)
                J_E: 'end grain' or 'other' {'end grain':0.67, 'other':1}
                J_A: 'toe-nail' or 'other' {'toe-nail':0.83, 'other':1} 
                J_B: 'clinched' or 'other' {'clinched':1.6, 'other':1}
                    (Only for 1 shear plane)
                J_D: 'diaphragm' or 'other' {'diaphragm':1.3, 'other':1}

                material object accepts Types: ('panel', 'SPF', 'CLT')
                material_1: Nail head side member (material object) 
                material_2: Middle memeber or second member (material object) 
                *Kwarg: peut accepter une troisième composition au besoins.
                    - material_3: Exterior member on the nail point side for
                    three shear plane system. (material object) 
                Nail: (nail object)  
                KD: load duration factor (default = 1)
                KSF: service condition (dry or wet) (default = 1)
                KT: Treatment (default = 1)
            
            Calculated object caracteristic:
                ns: number of shear planes per nail or spike
                f1: Embedment strength of side member, MPa
                f2: Embedment strength of main member, MPa
                f3: Embedment strength of main member where failure
                is fastener yielding, MPa
                fy: Nail or spike yield strength, MPa
                t2: Length of penetration into point-side member for
                two-member connections. Centre member thickness for
                three-member connections, mm
                nu: 
                Nu: 
                JF: 
                Nr: The factored lateral strength resistance of the nail or
                spike connection, N                 
        """
        # Constants
        self.nf=1
        self.phi=0.8
        
        # Arguments
        self.J_E=J_E
        self.J_A=J_A
        self.J_B=J_B
        self.J_D=J_D
        self.material_1=material_1
        self.material_2=material_2
        self.Nail=Nail
        
        # Keyword Arguments
        self.KD=KD
        self.KSF=KSF
        self.KT=KT
        self.material_3=kwarg.get('material_3')
        
        # Calculate object caracteristics
        self.calculate_object_caracteristics()

    def calculate_object_caracteristics(self):
        """
            This will initialize and update the calculated object
            caracteristics.
            Important to keep the variable asignation in this order.
        """
        self.ns=self.number_of_shear_planes()
        self.f2=self.calculate_f2()
        self.f3=self.calculate_f3()
        self.fy=self.calculate_fy()
        self.t1=self.calculate_t1()
        self.t2=self.calculate_t2()
        self.f1=self.calculate_f1()
        self.nu=self.minimum_nu_a_to_g()
        self.mode_a=self.mode_a()
        self.mode_b=self.mode_b()
        self.mode_c=self.mode_c()
        self.mode_d=self.mode_d()
        self.mode_e=self.mode_e()
        self.mode_f=self.mode_f()
        self.mode_g=self.mode_g()
        self.Nu=self.calculate_Nu()
        self.validate_J() # Updates erroneous values
        self.compatibility_J() # Avoids incompatibilities
        self.JF=self.calculate_JF()
        self.Nr=self.nail_lateral_resistance()
        return

# Utility function    
    def try_catch(func):
        def wrapper(*args,**kwargs): 
            try:
                fu = func(*args,**kwargs)
            except:
                print('Function failed to load')
                return
            return fu
        return wrapper
    
    def validate_J(self):
        """
            Function makes sure the proper J values are used.
            J_B: {'clinched':1.6, 'other':1}
            J_D: {'diaphragm':1.3, 'other':1}
            J_E: {'end grain':0.67, 'other':1}
            J_A: {'toe-nail':0.83, 'other':1}
        """
        if self.ns == 1:
            if self.J_B != 1.6 and self.J_B != 1.0:
                self.J_B = 1.0
            if self.J_D != 1.3 and self.J_D != 1.0:
                self.J_D = 1.0
        if self.ns == 2:
            self.J_B = 1.0  
            self.J_D = 1.0
        if self.J_E != 0.67 and self.J_E != 1.0:
            self.J_E = 0.67
        if self.J_A != 0.83 and self.J_A != 1.0:
            self.J_A = 0.83        
        return
 
    def compatibility_J(self):
        """
            Function that manages J factor conflicts
        """ 
        if self.J_A != 1.0:
            self.J_B = 1.0
            self.J_D = 1.0
        if self.J_A != 1.0 and self.J_E != 1.0:
            self.J_A = 0
            print('Can t have toe nail in end grain!')
        return
    
# Secondary functions
    def number_of_shear_planes(self):
        """
            Calculates the number of shear planes based on the presence of a
            third material in the object.            
        """
        if (self.material_3 is not None
            and self.material_1.Thick >= 3 * self.Nail.Dia
            and self.material_2.Thick >= 8 * self.Nail.Dia
            and self.Nail.Len - self.material_1.Thick -
            self.material_2.Thick >= 5 * self.Nail.Dia
            and self.material_3.Thick >= 5 * self.Nail.Dia):
            ns = 2
        elif (self.material_1.Thick >= 3 * self.Nail.Dia and
              self.Nail.Len - self.material_1.Thick >= 5 *
              self.Nail.Dia):
            ns = 1
        else:
            print('A geometric condition is out of the scope of the nail lateral reistance equation')
            ns = 0   
        return ns 

    def calculate_Jx (self,material):
        if material.Type == 'CLT':
            Jx = 0.9
        elif material.Type == 'SPF' or material.Type == 'CSP':
            Jx = 1
        else:
            Jx = 0
            print ('Enter valid material type for main member. See NailLateralRes function')
        return Jx

    def sub_calculate_f1(self, material):
        """
            f1: Embedment strength of side member, MPa
        """
        if material.Type == 'panel':
            f1 = 104 * material.G * (1 - 0.1 * self.Nail.Dia)
        elif material.Type == 'CLT' or material.Type == 'SPF':
            f1 = (50 * material.G * (1 - 0.01 * self.Nail.Dia) * 
            self.calculate_Jx(material))
        else:
            print('Error see calculate_f1 function')
            f1=0
        return f1
        
    def calculate_f1 (self):
        if self.ns == 1:
            self.f1 = self.sub_calculate_f1(self.material_1)
        elif self.ns ==2:
### We need to test if the self.nu will get updated when self.f1 changes.
            self.f1 = self.sub_calculate_f1(self.material_1)
            min_mode_mat_1 = self.minimum_nu_a_to_g()
            self.f1 = self.sub_calculate_f1(self.material_3)
            if self.minimum_nu_a_to_g() > min_mode_mat_1:
                self.f1 = self.sub_calculate_f1(self, material_1)
            else:
                print('Using material_3 properties to calculate f1')
        else:
            self.f1=None
        return self.f1

    def calculate_f2 (self):
        """
            f2 = embedment strength of main member, MPa
        """
        f2 = (50 * material_2.G * (1 - 0.01 * self.Nail.Dia) *
              self.calculate_Jx(material_2))
        return f2

    def calculate_f3 (self):
        """
            f3 = embedment strength of main member where failure is fastener
            yielding, MPa
        """
        f3 = (110 * material_2.G**1.8 * (1 - 0.01 * self.Nail.Dia) *
              self.calculate_Jx(material_2))
        return f3

    def calculate_fy (self):
        """
            fy = nail or spike yield strength, MPa
        """
        fy = 50 * (16 - self.Nail.Dia) 
        return fy

    def calculate_t1 (self):
        """
        t1 = head-side member thickness for two-member connections, mm
        t1 = minimum side plate thickness for three-member connections, mm
        """
        if self.ns == 1:
            t1 = self.material_1.Thick
        elif self.ns == 2:
            t1 = 3 * self.Nail.Dia
        else:
            print('Invalid number of shear planes')
            t1 = 0            
        return t1
    
    def calculate_t2 (self):
        """
            t2 = length of penetration into point-side member for two-member connections, mm
            t2 = centre member thickness for three-member connections, mm
        """
        t2 = min(self.Nail.Len - self.material_1.Thick, self.material_2.Thick)
        return t2
   
# The unit lateral strength resistance, nu (per shear plane),
# shall be taken as the smallest value calculated in accordance
# with Items (a) to (g).
    @try_catch
    def mode_a (self):
        nu_a = self.f1 * self.Nail.Dia * self.t1
        return nu_a
    @try_catch    
    def mode_b (self):
        nu_b = self.f2 * self.Nail.Dia * self.t2
        return nu_b
    @try_catch
    def mode_c (self):
        nu_c = 0.5 * self.f2 * self.Nail.Dia * self.t2
        return nu_c
    @try_catch
    def mode_d (self):
        nu_d = (self.f1 * self.Nail.Dia**2 * (((self.f3 * self.fy) /
               (6 * (self.f1 + self.f3) * self.f1))**0.5 + self.t1 /
               (5 * self.Nail.Dia)))
        return nu_d
    @try_catch
    def mode_e (self):
        nu_e = (self.f1 * self.Nail.Dia**2 * (((self.f3 * self.fy) /
               (6 * (self.f1 + self.f3) * self.f1))**0.5 + self.t2 /
               (5 * self.Nail.Dia)))
        return nu_e
    @try_catch
    def mode_f (self):
        nu_f = (self.f1 * self.Nail.Dia**2 /5 * (self.t1 / self.Nail.Dia +
                (self.f2 * self.t2) / (self.f1 * self.Nail.Dia)))
        return nu_f
    @try_catch
    def mode_g (self):
        nu_g = self.f1 * self.Nail.Dia**2 * (2 / 3 * (self.f3 * self.fy) /
                ((self.f1 + self.f3) * self.f1))**0.5 
        return nu_g

    def minimum_nu_a_to_g (self):
        try:
            if self.ns == 1:
                min_mode = min(self.mode_a(),self.mode_b(),self.mode_d(),
                               self.mode_e(),self.mode_f(),self.mode_g())
                print('ns = 1 mode')
            elif self.ns ==2:
                min_mode = min(self.mode_a(),self.mode_c(),self.mode_d(),
                               self.mode_g())
                print('ns = 2 mode')
            else:
                min_mode = 0
        except:
            min_mode = 0
        return min_mode
    
    def calculate_Nu (self):
        Nu = self.nu * self.KD * self.KSF * self.KT      
        return Nu
    
    def calculate_JF (self):
        JF = self.J_E * self.J_A * self.J_B * self.J_D
        return JF

# Main function
    def nail_lateral_resistance (self):
        """
            12.9.4.1, The factored lateral strength resistance of the nail or
            spike connection, Nr , shall be taken as follows:
            Nr = φ Nu nF nS JF
            
            This function evaluates the lateral resistance for one fastener.
            result can be multiplied by the number of fastener to have a groupe
            resistance.
        """
### Validate if object is changed that everything follows.
        Nr = self.phi * self.Nu * self.nf * self.ns * self.JF
        return Nr        
    
 


###
        ####
                ####
                        ####
### Testing commands bellow:

print('Step 1 ----------------------------------------------------')
material_1 = Material(0.42,12,'panel')
material_2 = Material(0.42,38,'SPF')
material_3 = Material(0.42,300,'CLT')
Nail = Nail(3.048, 76.2)


Object1 = O86_14_2017(1,1,1,1,material_1,material_2,Nail,material_3=material_3)
print('Step 2 ----------------------------------------------------')
print(str(vars(Object1)))


Object1 = O86_14_2017(1,1,1,1,material_1,material_2,Nail)
print('Step 3 ----------------------------------------------------')
print(str(vars(Object1)))


print('Step 4 ----------------------------------------------------')
print('this is mode_a: '+str(Object1.mode_a))

Object1 = O86_14_2017(0.67,0.83,1,1,material_1,material_2,Nail)
print('Step 5 ----------------------------------------------------')
print(str(vars(Object1)))



#print('Step 5 ----------------------------------------------------')
#Nail.Len = 20
#Object1 = O86_14_2017(1,1,1,1,material_1,material_2,Nail)
#print('Self.ns when nail fail: '+str(Object1.ns))




#### Below is unrefined code -------------------v


  

#
##-------------------------------------------
## Equation for minimum spacing.
##-------------------------------------------
#
#def NailSpacing_A (Nail):
#    '''
#        This function is based on the CSA O86-14
#        12.9.2.1 Placement of fasteners in side grain    
#        This function returns a rounded up value to the 1/2"
#    '''
#
#    try:
#        # a: Spacing parallel to grain (16 x nail diameter for SPF lumber)
#        OC = Nail.Dia * 16
#        # round up to the 1/2"
#        OC = math.ceil(OC * 2) / 2
#    except:
#        OC = 999999
#        print('Invalid nail diameter')
#    
#    return OC
#










































