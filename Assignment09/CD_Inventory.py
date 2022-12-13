#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# STveter, 2022-Dec-11, Began work on this segment of the project
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        print('Quitting program')
        break
    
    
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('\n')
            print('reloading from file...')
            print('\n')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling program, please type \'yes\' to reload date. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  
        
        
        
        
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  
        
        
        
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue 
        
        
        
        
        
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODO add code to handle tracks on an individual CD
        while True:
            
            IO.ScreenIO.print_CD_menu()
            
            strChoice = IO.ScreenIO.menu_CD_choice()
            
            if strChoice == 'x':
                print('Quitting program')
                break
            
            
            if strChoice == 'a':
                tplTrkInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrkInfo)
                
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                trk_idx = input('Select the Track Index: ')
                cd.rmv_track(trk_idx)
                
            else:
                print('Please input one of the provided options')
                break
        
        
        
        
        
        
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? Enter [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
            print('Inventory successfully saved!!')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  
        
        
        
        
    else:
        print('Please input one of the provided options')
        print('\n')