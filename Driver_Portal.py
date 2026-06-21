# Keep these lists outside the class so they are easy to import elsewhere
avail_drivers = []  
unavail_drivers = [] 

class Driver:
    def __init__(self, name, status, vehicle, age=None):
        self.name = name
        self.age = age
        self.vehicle = vehicle.replace(' ', '').lower()  # Standardizes text format automatically
        self.status = status.strip().lower()

    @classmethod
    def recruit_driver(cls):
        """Onboards new drivers and adds them directly to the global lists outside."""
        print("\n========================================")
        print("      🛡️ DRIVER ONBOARDING PORTAL       ")
        print("========================================")
        
        while True:
            new_recruit = input("Do you want to register a new driver? (yes/no): ").strip().lower()
            
            if new_recruit == 'yes':
                name_of_recruit = input("👤 Enter Name: ").strip()
                age_of_recruit = int(input("🎂 Enter Age: "))
                car_of_recruit = input("🚘 Enter Vehicle Name/Model: ").strip()
                
                # Spawns a brand new Driver object instance
                new_driver = cls(name_of_recruit, 'online', car_of_recruit, age_of_recruit)
                
                # Adds it directly to the global list sitting outside the class
                avail_drivers.append(new_driver)
                print(f"✨ [SUCCESS] {name_of_recruit} is officially onboarded!\n")
                
            elif new_recruit == 'no':
                print("👋 Closing onboarding portal.")
                print("========================================\n")
                break
            else:
                print("⚠️  Invalid choice! Please type 'yes' or 'no'.")


# --- Adding the Initial Driver ---
driver1 = Driver('Yadav JI', 'Online', 'alto800', '23')

if driver1.status == 'online':
    avail_drivers.append(driver1)
else:
    unavail_drivers.append(driver1)


# --- For Testing Locally ---
if __name__ == "__main__":
    Driver.recruit_driver()
