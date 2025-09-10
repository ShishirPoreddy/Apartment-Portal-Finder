import re
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

class Apartment:
    
    def __init__(self):
        #Member who worked on this method: Avi
        #Technique used: Sequence unpacking
        
        # Read the CSV files
        self.apartments_df = pd.read_csv(r"CP Apartments_Version3.csv")
        self.amenities_df = pd.read_csv(r"Amenitites_Version2.csv")
        self.historical_df = pd.read_csv(r"Major Historical Data_Version3.csv")
        
        # Merging operation on Pandas DataFrames
        self.merged_data = self.apartments_df.merge(self.amenities_df, 
                                                    on=["Apartment Name"])
        
            
        # Will be used in the future:
            # Store the apartment names and minimum budgets in a dictionary
            #self.min_budgets = dict(zip(self.merged_data["Apartment Name"], 
            # self.merged_data["Minimum Price"]))
            
        self.terrapin_row, self.university_view, self.the_varsity, self.south_campus_commons = self.merged_data["Apartment Name"].unique()
        self.min_budget = {"Terrapin Row":1250, "University View":1200, 
                           "The Varsity":1104, "South Campus Commons":1016} 
        
        
        self.major_campus_dictionary=  {1: ["University View","The Varsity"],
                                   2:["Terrapin Row","South Campus Commons"],
                                   3: ["Terrapin Row","South Campus Commons"],
                                   4:["University View","The Varsity"],
                                   5:["Terrapin Row","South Campus Commons"]}
        
             
       
        # Initialize user attributes to None
        self.user_name = None
        self.proofOfIdentity = None
        self.proofOfIncome = None
        self.proof_of_identity_boolean = False
        self.proof_of_income_boolean = False
        self.user_budget = None
        self.user_location = None
        self.user_pool = None
        self.user_gym = None
        self.user_parking = None
        self.user_electronic_entry_locks = None
        self.user_study_rooms = None
        self.user_game_lounge = None
        self.user_input_budget=None  
        self.major_category_input=None
        self.apartment1=None
        self.apartment2=None
        
        # User's chosen apartment attributes
        self.chosen_apartment=None
        self.num_people=None
        self.chosen_apartment_budget=None
        
        # User's profile attributes
        self.full_name = None
        self.email = None
        self.phone = None
        

    def amenityCheck(self,apt1,apt2,amenity):
        #Member who worked on this method: Philip
        #Technique used: Filtering operation on Pandas DataFrames
        apartment1_amenity = self.amenities_df.loc[self.amenities_df ['Apartment Name'] == apt1, amenity].values[0]
        apartment2_amenity = self.amenities_df.loc[self.amenities_df ['Apartment Name'] == apt2, amenity].values[0]
        
        if apartment1_amenity == 1:
            print(f"{apt1} has a {amenity}.")
        else:
            print(f"{apt1} does not have a {amenity}.")

        if apartment2_amenity == 1:
            print(f"{apt2} has a {amenity}.")
        else:
            print(f"{apt2} does not have a {amenity}.")  
            
            
    def userBudget(self, someUserBudget, apt1, apt2):
        #Member who worked on this method: Shishir
        #Technique used: List comprehension
        apt1_minBudget=self.min_budget[apt1]
        apt2_minBudget=self.min_budget[apt2]
        
        aptAndMinBudget=[apt1_minBudget,apt2_minBudget]
        cheapest_apt_value=min(aptAndMinBudget)
        #list comprehension: used to reverse keys and values of a dict in order to display the name of the cheapest apt
        reversed_minBudget={value: key for key, value in self.min_budget.items()}
        name_of_cheapest_apt = reversed_minBudget[cheapest_apt_value]
        
        if someUserBudget >= apt1_minBudget and someUserBudget >=apt2_minBudget:
            print(f"You can afford the minimum monthly rent at both {apt1} and {apt2}.")
            print(f"The cheapest apartment on your side of campus is {name_of_cheapest_apt} (${cheapest_apt_value}).")
        elif someUserBudget >= apt1_minBudget:
            print(f"You can afford the monthly rent at {apt1} only.")
        elif someUserBudget >= apt2_minBudget:
            print(f"You can afford the monthly rent at {apt2} only.")
        else:
            print(f"You cannot afford the minimum monthly rent at either apartments.")
        
        # matching_apartments = [key for key in self.min_budget if 
        #                        self.min_budget[key] <= self.user_input_budget]
        # if not matching_apartments:
        #     raise ValueError("Your budget does not meet the minimum budget" 
        #                      " for any of the apartments")
        # elif self.user_input_budget >= self.min_budget["Terrapin Row"]:
        #     print (f'Your budget satisfies the minimum budget of all the'
        #            ' apartments:' 
        # f' Terrapin Row:({self.min_budget["Terrapin Row"]}), University View:' 
        # f' ({self.min_budget["University View"]}), and The Varsity:' 
        # f' ({self.min_budget["The Varsity"]})')
        # elif self.user_input_budget >= self.min_budget["University View"]:
        #     print (f'You meet the minimum budget of University View:'
        #     f' {self.min_budget["University View"]}')
        # else:
        #     print (f'You meet the minimum budget of The Varsity:' 
        #     f'{self.min_budget["The Varsity"]}')
            
        #STEP 2 :CALCULATE ADDITIONAL EXPENSES (EXPENSES THE MONTHLY RENT DOES NOT COVER)
       # Additional expenses:
         
      
       #STEP 3 :DOES USER HAVE ENOUGH MONEY TO PAY RENT FOR THEIR DURATION (FULL YEAR OR HALF A YEAR) OF STAY
       
        # Will be used in the future:
            #return cheapest_apt
            #Or find a way to use cheapest_apt later in this program.   
          
    def check_eligibility(self, some_name, proof_of_identity, proof_of_income):
        """
        Check if user meets all the proper documentation for leasing.

        Args:
        - identity_proof: string, proof of identity (e.g. driver's license, 
            passport)
        - income_proof: string, proof of income (e.g. pay stub, 
            bank statement)
        - residency_proof: string, proof of current residency (e.g. utility 
            bill, lease agreement)
        - insurance_proof: string, proof of insurance (e.g. auto insurance, 
            renters insurance)

        Returns:
        - eligible: boolean, True if user meets all the proper documentation, 
            False otherwise
        """
        #Member who worked on this method: Jhemel
        #Technique used: Conditional Expression
        
        
        

        
        if proof_of_identity == "yes" and proof_of_income == "yes":
            print(f"{some_name}, you are eligible to lease an apartment in College Park.")
            self.proof_of_identity_boolean = True
            self.proof_of_income_boolean = True

        elif proof_of_identity == "yes" and proof_of_income == "no":
            print(f"{some_name}, you are not eligible to lease an apartment in College Park." 
            "\nPlease provide proof of income to proceed further.")
            self.proof_of_identity_boolean = True
            self.proof_of_income_boolean = False
        elif proof_of_identity == "no" and proof_of_income == "yes":
            print(f"{some_name}, you are not eligible to lease an apartment in College Park." 
            "\nPlease provide proof of identity to proceed further.")
            self.proof_of_identity_boolean = False
            self.proof_of_income_boolean = True
        else:
            return(f"{some_name}, you are not eligible to lease an apartment in College Park.")
        
        result = "Identity and income verified." if proof_of_identity == True and proof_of_income == True else "Identity and/or income not verified"
        print(result)

        # Will be used in the future:
            # Check if the user meets the minimum income requirement
            #min_income_requirement = 30000  # set a minimum income requirement of $30,000
            #if income_proof < min_income_requirement:
                
                #print("Your income does not meet the minimum requirement.")
                #return False
            
            # Check if the residency proof is current
            # You could implement this check by comparing the date on the residency_proof to today's date
            
            # Check if the insurance proof is valid
            # You could implement this check by verifying that the insurance policy is currently active
            
            # If all checks pass, the user is eligible
            #print("Congratulations, you are eligible to lease!")
            #return True    
                
        #Prof's advice: 
        #  Make the method more generic 
        #  return True if eligible or False if not eligible
            
        
        # Will be used in the future:
            # Check if the user meets the minimum income requirement
            #min_income_requirement = 30000  # set a minimum income requirement of $30,000
            #if income_proof < min_income_requirement:
                
                #print("Your income does not meet the minimum requirement.")
                #return False
            
            # Check if the residency proof is current
            # You could implement this check by comparing the date on the residency_proof to today's date
            
            # Check if the insurance proof is valid
            # You could implement this check by verifying that the insurance policy is currently active
            
            # If all checks pass, the user is eligible
            #print("Congratulations, you are eligible to lease!")
            #return True
    
    def find_shared_group_apartment(self, num_people, some_apartment, budget):
        """
        Finds apartments that can accommodate a group of people with the given criteria.

        Args:
        - num_people (int): The number of people who want to live together in the apartment.
        - some_apartment (str): The apartment chosen by the user.
        - budget (float): The monthly rent per person in the group for the chosen apartment.
        Returns:
        - A list of apartments that meet the given criteria.
        """
    # #Techniques used: f-strings containing expressions
    # #Member who worked on this method: Jhemel
    # Assume we have a list of available apartments with their details
        chosen_apartment_df =  self.apartments_df[ self.apartments_df['Apartment Name'] == self.chosen_apartment]
        #print(chosen_apartment_df)
        chosen_rooms_available_df = chosen_apartment_df[chosen_apartment_df['Number of Rooms Available']>= self.num_people ]
        print("\nThese are the rooms available that can fit the number of tenants:")
        print(chosen_rooms_available_df)

        chosen_apartment_number = int(input("\nWhich of the apartment units listed best fit your needs?"
        "\nPlease specify the Apartment Number of the unit shown under the Apartment Number column (e.g. 500):" ))
        apartment_number_df = chosen_apartment_df[chosen_apartment_df['Apartment Number']== chosen_apartment_number]
        
        #f-strings containing expressions
        print(f"\n{self.user_name}, this is the apartment unit's information:")
        print(apartment_number_df)
        
        #f-strings containing expressions
        print(f"This is the monthly rent that each of the tenants have to pay (including you): ${budget}.")
    
    def submitApplication(self, some_apartment, some_name, some_email, some_Phone):
        #Member who worked on this method: Avi
        #Technique used: regular expressions
        name=None
        email=None
        phone=None
        
        validated_dict = {name:some_name, email:some_email, phone:some_Phone}
        
        # validate user input with regular expressions
        name_regex = r'[A-Za-z]\S+ .+?[A-Za-z\d]+$'
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        phone_regex = r'^\d{3}-\d{3}-\d{4}$'
        
        if not re.match(name_regex, some_name):
            print("Invalid name. Please enter a valid name.")
            
        
        if not re.match(email_regex, some_email):
            print("Invalid email. Please enter a valid email address.")
            
        
        if not re.match(phone_regex, some_Phone):
            print("Invalid phone number. Please enter a valid phone number in the format xxx-xxx-xxxx.")
        
        for key in validated_dict:
            if (not re.match(name_regex, str(validated_dict[key]))) and \
            (not re.match(email_regex, str(validated_dict[key]))) and \
            (not re.match(phone_regex, str(validated_dict[key]))):
                return False
        return True

            # if key in validated_dict != name_regex & key in validated_dict != email_regex & key in validated_dict != phone_regex:
            #     return False   
            # else: 
            #     return True
                    
    def amenities_rsvp(self, some_apartment, some_amenity='Study Rooms'):
        #Member who worked on this method: Shishir
        #Technique used:optional parameters
        print(f"For {some_apartment}, we've reserved this {some_amenity} for you. ")
              
    def userInput(self):
        #Member who worked on this method: Philip
        #Technique used:Visualizing data with seaborn 
        
        #INTRODUCTION
        print("Welcome to the College Park Apartment Portal!\n \nThere are four "
              "apartments for you to choose from in the College Park Area:"
              "\n Terrapin Row, \n University View, " 
              "\n The Varsity, and \n South Campus Commons.")
        print("\nTerrapin Row and South Campus Commons are located in "
              "South campus.")
        print("\nUniversity View and The Varsity are located in North campus.")
        print("\nAnswer some questions to find your ideal apartment!")

        self.user_name = input("\nPlease enter your full name:")
        
        print(f"\nHi {self.user_name}! In order to proceed with the rest of "
              "the College Park Apartment Portal, \nwe have to check if you "
              "meet all the eligibility requirements.") 
        self.proofOfIdentity = input("Do you have a Driver's License or a Passport? (yes/no): ")
        self.proofOfIncome = input("Do you have a Pay Stub or a Bank Statement? (yes/no): ")

        self.check_eligibility(self.user_name, self.proofOfIdentity,self.proofOfIncome)

        while self.proof_of_identity_boolean == False or self.proof_of_income_boolean == False:
            self.proofOfIdentity = input("Do you have a Driver's License or a Passport? (yes/no): ")
            self.proofOfIncome = input("Do you have a Pay Stub or a Bank Statement? (yes/no): ")
            self.check_eligibility(self.user_name, self.proofOfIdentity,self.proofOfIncome)
            
        
        #Prof's advice: Stops the questions for the ineligible user:
        #if self.check_eligibility() == False:
        #   return #Purpose of this return is to end function

        #Mention eligilibility txt file upload requirements in documentation.
        # At this point of the program, provide this file... (brief)
        
        
        #MAJOR CATEGORIES
        self.major_category_input = int(input("\nWhich one of the following categories "
                                     "would your major fall under?\n"
          "Type 1 for STEM (Classes in North campus)\n"
          "Type 2 for Business (Classes in South campus)\n"
          "Type 3 for Public Policy (Classes in South campus)\n"
          "Type 4 for Fine Arts (Classes in North campus)\n"
          "Type 5 for Architecture (South campus)\n"))
        
        major_number_dictionary = {1:"STEM",2:"Business", 3:"Public Policy",
                                     4:"Fine Arts",5:"Architecture"}
        
        
        major_proximity_dictionary = {1:"University View and The Varsity "
                                     "are located near STEM buildings",
                                     2:"Terrapin Row and South Campus Commons "
                                     "are located near Business buildings",
                                     3:"Terrapin Row and South Campus Commons "
                                     "are located near Public Policy buildings",
                                     4:"University View and The Varsity "
                                     "are located near Fine arts buildings",
                                     5:"Terrapin Row and South Campus Commons "
                                     "are located near Architecture buildings"}
        print(major_proximity_dictionary[self.major_category_input])
        
        
        print(f"\nLet's see what most "
              f"{major_number_dictionary[self.major_category_input]} majors in "
              f"previous years chose as their apartment.\n")
        #Visualizing historical data with seaborn
        
        #Filter historical database by user's specific major.
        df_major = self.historical_df[self.historical_df["Major"] 
                        == (major_number_dictionary[self.major_category_input])]
        sns.countplot(x = "Apartment", data = df_major)
        plt.show()
        
        if self.major_category_input == 1 or self.major_category_input == 4:
            print("\nBetween University View and The Varsity, let's see which "
                  "apartment best fits your amenity needs.")
        else: 
            print("\nBetween Terrapin Row and South Campus Commons, let's pick one "
                  "apartment that best fits your amenity needs.")   
            
        #The two apartments in the side of campus where the user's classes 
        # for major are.
        self.apartment1 = self.major_campus_dictionary[self.major_category_input][0]
        self.apartment2 = self.major_campus_dictionary[self.major_category_input][1]
         
        #Amenities questions (make this its own method in the future)
            #'Pool' question and check
        user_pool=int(input("\nAre you looking for a pool? Type 0 for no pool or 1"  
                        " for pool:"))
        self.amenityCheck(self.apartment1,self.apartment2, 'Pool')
        
            #'Gym'question and check
        user_gym=int(input("\nAre you looking for a gym? Type 0 for no gym or 1" 
                        " for gym:"))
        self.amenityCheck(self.apartment1,self.apartment2, 'Gym')
        
            #'Parking' question and check
        user_parking=int(input("\nAre you looking for parking? Type 0 for no" 
                            " parking and 1 for parking:" ))
        self.amenityCheck(self.apartment1,self.apartment2, 'Parking')
            
            #'Electronic Key Locks' question and check
        user_electronic_entry_locks=int(input("\nDo you want an apartment with an"
                                        " electronic entry lock system? Type 0"
                                        " for no system and 1 for a system:"  )) 
        self.amenityCheck(self.apartment1,self.apartment2, 'Electronic Key Locks')
        
            #'Study Rooms' question and check
        user_study_rooms=int(input("\nAre you looking for study rooms? Type 0 for"
                               " no study rooms and 1 for study rooms:"))
        self.amenityCheck(self.apartment1,self.apartment2, 'Study Rooms')
            
            #'Game Lounge' question and check
        
        user_game_lounge=int(input("\nAre you looking for game lounge? Type 0 for" 
                                   " no game lounge and 1 for a game lounge:"))
        self.amenityCheck(self.apartment1,self.apartment2, 'Game Lounge')
    
        # BUDGET QUESTIONS
        self.user_input_budget = int(input("\nWhat is your minimum budget?")) 
        self.userBudget(self.user_input_budget, self.apartment1, self.apartment2)

        # APARTMENT SUMMARY (do this later)
        # State the amenities available at apt1 and apt2.
        # Restate the cheapest apt
        
        # PICK ONE APARTMENT
        self.chosen_apartment = input(f"Between {self.apartment1} and " 
                                     f"{self.apartment2}, \nplease write down "  
                                     f"the apartment you prefer to stay in "
                                     f"based on your preferences:\n")
        if self.chosen_apartment == self.apartment1:
            self.chosen_apartment = self.apartment1
            #return self.chosen_apartment
        else:
            self.chosen_apartment = self.apartment2
            #return self.chosen_apartment
        otherTenants = (input(f"\n{self.user_name}, are you looking "
                                    f"to move into {self.chosen_apartment} "
                                    f"with other tenants? (y/n)"))
        if otherTenants == "y":
            self.num_people = int(input("\nHow many tenants are moving in "
                                     "with you (including yourself)? 1,2,3,or 4?"))
            self.chosen_apartment_budget = self.min_budget[self.chosen_apartment]
            self.find_shared_group_apartment(self.num_people, self.chosen_apartment, self.chosen_apartment_budget)
        else:
            print("That's it!")
            
        # ENTER USER PROFILE DETAILS
        # check if user is logged in
        self.user_name=input("enter your username(must be within 9 characters): ")
        
        while len(self.user_name)>9:
             self.user_name=input("enter your username(must be within 9 characters): ") 
        else:
            print(f"your username is {self.user_name}")        
        
        # get user input
        self.full_name = input("Please enter your full name:")
        self.email = input("Please enter your email address:")
        self.phone = input("Please enter your phone number (format: xxx-xxx-xxxx):")

        applicationCall = self.submitApplication(self.chosen_apartment, self.full_name, self.email, self.phone)
        thankyou_message = False
         
        while applicationCall == False:
            # get user input
            self.full_name = input("Please enter your full name:")
            self.email = input("Please enter your email address:")
            self.phone = input("Please enter your phone number (format: xxx-xxx-xxxx):")
            
        
                    
            if self.submitApplication(self.chosen_apartment, self.full_name, self.email, self.phone):
                # if user input is valid, submit application
                print(f"Thank you, {self.full_name}, for submitting your application to {self.chosen_apartment}. We will contact you soon.")
                thankyou_message = True
                applicationCall = True
            else:
                print("Please enter valid information.")
                
        else:
            if thankyou_message == False:
                print(f"Thank you, {self.full_name}, for submitting your application to {self.chosen_apartment}. We will contact you soon.")
            else:
                exit
                
        print("Once you join our apartment you can make reservations for the amenities we offer. ")
        self.reserve_amenity = input("Which of the following amenities would you like to reserve: Pool, Study Rooms, or Game Lounge?\n"
                                     "Please use exact spelling. If you don't specify an amenity and type a space, Study Rooms will be chosen by default\n"
                                     "since it is offered as an amenity at all College Park apartments. \nWhich amenity?: ")
        
        if self.reserve_amenity == " ":
            self.amenities_rsvp(self.chosen_apartment)
        else:
            self.amenities_rsvp(self.chosen_apartment, self.reserve_amenity)
                
        

        
    


        
   

#We will implement this main method in the future.
def main():
    apt = Apartment()
    
    apt.userInput()
    
    
if __name__=='__main__':
    main()

        



            
        
   
              
                
                







