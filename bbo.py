import sys
import csv
import constants
import pyperclip

AllOrigins = constants.AllOrigins
OtherCanada = constants.OtherCanada
OtherMountainStates = constants.OtherMountainStates
OtherSouthernStates = constants.OtherSouthernStates
MidwestStates = constants.MidwestStates
NewEnglandStates = constants.NewEnglandStates
MiddleAtlantic = constants.MiddleAtlantic
SouthAtlantic = constants.SouthAtlantic
HawaiiandAlaska = constants.HawaiiandAlaska
Australia = constants.Australia
Japan = constants.Japan
Mexico = constants.Mexico
UnitedKingdom = constants.UnitedKingdom
Brazil = constants.Brazil

def getInputfilepath():
    mfr_path = input("\nFile path (Market Feeder Report): ")
    return mfr_path

def main():
    mfrPath = getInputfilepath()
    try:
        with open(mfrPath, newline='') as mfrFile:
            mfrReader = csv.reader(mfrFile,delimiter=',', quotechar='|')

            # skip the first line that contain header
            next(mfrReader)
            # total
            totalBookings = 0
            #assign each states data to the dictionary
            for line in mfrReader:
                state = line[1]
                bookings = int(line[2])
                totalBookings += bookings
                if state in AllOrigins:
                    AllOrigins[state] += bookings
                elif state in OtherCanada:
                    AllOrigins["Canada Other"] += bookings
                elif state in OtherMountainStates:
                    AllOrigins["Other Mountain States"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in OtherSouthernStates:
                    AllOrigins["Other Southern States"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in MidwestStates:
                    AllOrigins["Midwest States"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in NewEnglandStates:
                    AllOrigins["New England States"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in MiddleAtlantic:
                    AllOrigins["Middle Atlantic"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in SouthAtlantic:
                    AllOrigins["South Atlantic"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in HawaiiandAlaska:
                    AllOrigins["Hawaii/Alaska"] += bookings
                    AllOrigins["US Total"] += bookings
                elif state in Australia:
                    AllOrigins["Australia"] += bookings
                elif state in Japan:
                    AllOrigins["Japan"] += bookings
                elif state in Mexico:
                    AllOrigins["Mexico"] += bookings
                    AllOrigins["Other Countries"] += bookings
                elif state in UnitedKingdom:
                    AllOrigins["United Kingdom"] += bookings
                    AllOrigins["Europe Total"] += bookings
                elif state in Brazil:
                    AllOrigins["Brazil"] += bookings
                    AllOrigins["Other Countries"] += bookings
                else:
                    AllOrigins["Other Unknown"] += bookings 
    
        # Canada tatal
        AllOrigins["Canada Total"] = AllOrigins["British Columbia"] + AllOrigins["Alberta"] + AllOrigins["Ontario"] + AllOrigins["Quebec"] + AllOrigins["Canada Other"]
    
        # US total
        AllOrigins["US Total"] += AllOrigins["Washington"] + AllOrigins['Oregon'] + AllOrigins['California'] + AllOrigins['Arizona'] + AllOrigins['Texas'] + AllOrigins['New York']

        # Asia Pacific Total
        AllOrigins["Asia Pacific Total"] = AllOrigins['Australia'] + AllOrigins['Japan']

        # Other country Total
        AllOrigins['Other Country Total'] =  AllOrigins['Other Countries'] + AllOrigins['Other Unknown']

        # Grand Total
        AllOrigins['Grand Total'] = totalBookings
    
        # Copy to clipboard
        pyperclip.copy('\n'.join([str(s) for s in AllOrigins.values()]))
        
        print('\nSuccess: Results are copied to clipboard')

    except IOError as e:
        print(e)
    except:
        print('\nError: something is wrong!')

def header():
    print(''.join('*' for i in range(43)))
    print('\n***\tBooking Breakdown by Origin\t***\n')
    print(''.join('*' for i in range(43)))
    print('')

def footer():
    input('\n\n***\tPress any key to exit the program.')
if __name__ == "__main__":
    header()
    main()
    footer()
