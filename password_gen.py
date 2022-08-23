import random
import Faker


#current year



    
current_year   = datetime.datetime.now().year
    
def generate_suffix():
    #choose one of the following suffixes and return it
    suffix = random.choice(['','','!',current_year,current_year+"!"])

    return suffix



def generate_prefix():
    prefix = random.choice(['Best','','!',current_year,current_year+"!"])
    
    
    
    
    
    
    
    
    
    
    
def password_pattern_gen(suffix,prefix,length):
    pass



    