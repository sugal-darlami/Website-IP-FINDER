import os
print("====================")
print("    NMAP HELPER")
print("====================")
target =input ("Enter target ip or website: ")
print ("Choose scan")
print ("1. Syn")
print ("2. Connect")
print ("3. version")
print ("4. OS")
print ("5. Aggressive")
print ("6. Ping")
print("----------------------------")
choice =input("Enter your choice: ")
if choice =="1":
    os.system(f"nmap -sS {target}")
elif choice == "2":
    os.system(f"nmap -sT {target}")

elif choice == "3":
    os.system(f"nmap -sV {target}")

elif choice == "4":
    os.system(f"nmap -O {target}")

elif choice == "5":
    os.system(f"nmap -A {target}")

elif choice == "6":
    os.system(f"nmap -sn {target}")

else:
    print("Invalid option")
