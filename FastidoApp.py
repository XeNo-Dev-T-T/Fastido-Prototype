from Drivers import avail_drivers, Driver, unavail_drivers
import random

class Wallet:
    def __init__(self, wallet_balance=500):
        self.wallet_balance = wallet_balance

    def transfer(self, amount):
        # Prevent transaction if fare exceeds the available cash balance
        if self.wallet_balance >= amount:
            self.wallet_balance -= amount
            print("\n========================================")
            print("💳 [SUCCESS] Transaction complete!")
            print(f"💰 Fare Deducted:    ₹{amount}")
            print(f"💳 Remaining Cash:   ₹{self.wallet_balance}")
            print("========================================\n")
            return True
        else:
            print("\n❌ [DECLINED] Insufficient funds! You cannot scam the system.")
            return False

    def display_balance(self):
        print(f"Account Balance: ₹{self.wallet_balance}")
        
        
class FastidoApp:
    def __init__(self):
        # Keeping core lists and session properties organized in memory
        self.avail_drivers = avail_drivers
        self.unavail_drivers = unavail_drivers
        self.user_wallet = Wallet(500) 
        self.user_name = ""
        self.distance = 0
        self.user_driver = None
        self.amount = 0

    def Welcome(self):
        print("========================================")
        print("          WELCOME TO FASTIDO APP         ")
        print("========================================")
        self.user_name = input("👤 Enter Your Name: ").strip()
        
        while True:
            user_request = input("🚗 Would you like to request a ride? (y/n): ").lower().strip()
            if user_request == 'n':
                print("👋 Keeping the app open for other users...\n")
                continue
            elif user_request == 'y':
                print("\n⚙️  Setting up the workspace environment...")
                break
            else:
                print("⚠️  Invalid choice! Please type 'y' or 'n'.")

    def get_distance(self):
        while True:
            try:
                # Store distance directly onto the class object to avoid variable scoping bugs
                self.distance = int(input("\n📍 Enter total travel distance (in KMS): "))
                if self.distance <= 0:
                    print("⚠️  Distance must be a positive number. Try again.")
                    continue
                else:
                    print("🏁 Destination logged. Heading to the next checkpoint!")
                    break
            except ValueError:
                print("⚠️  Please enter a valid whole number.")
        self.get_cartype()

    def get_cartype(self):
        car = input("🚘 Enter preferred vehicle model (e.g., Alto 800): ").strip()
        
        # Look inside the list of objects for matching vehicle strings
        matching_driver = []
        for d in self.avail_drivers:
            if d.vehicle.lower() == car.lower():
                matching_driver.append(d)
        
        if not matching_driver:
            print("❌ No matching online drivers found for this car model. Exiting...")
            return False
            
        self.user_driver = random.choice(matching_driver)
        print(f"\n✨ [FOUND] Driver Assigned: {self.user_driver.name}")
        self.assign_driver()

    def assign_driver(self):
        storage = {
            self.user_driver: self.user_name
        }
        print("📡 Dispatching driver to your current coordinates...")
        self.ride_confirmation()

    def ride_confirmation(self):
        timely = input("\n❓ Has the driver arrived at your pickup point? (yes/no): ").strip().lower()
        if timely == 'yes':
            print("🎒 Onboarded! Wishing you a safe and happy journey.")
        elif timely == 'no':
            print("⏳ Please hold on a moment while the driver navigates traffic...")
            self.ride_confirmation()
            return  # Halts old recursion threads from leaking downwards
        else:
            print("⚠️  Please provide a straightforward 'yes' or 'no'.")
            self.ride_confirmation()
            return 

        # Calculate absolute fare (Fixed rate of ₹8 per KM)
        self.amount = 8 * self.distance
        
        while True:
            arrived = input("\n🏁 Have you reached your final destination? (yes/no): ").strip().lower()
            if arrived == 'yes':
                print("\n📱 Initializing payment gateway...")
                break
            else:
                print("🚗 Driving along the route... checking status again.")
                continue
                
        # Send dynamic amount data to the separate object session
        self.user_wallet.transfer(self.amount)
        self.goodbye()

    def goodbye(self):
        print("========================================")
        print("     🙏 Thank you for riding with us!   ")
        print("========================================\n")


# --- RUN THE APP HERE ---
if __name__ == "__main__":
    app = FastidoApp() 
    app.Welcome()       
    app.get_distance()  
