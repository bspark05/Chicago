'''
Created on Jun 18, 2015

@author: Bumsub
'''
import Web.APIs.ChicagoOpendata.ChicagoAPI as COD
import shapefile
import csv
import time

def setField_TT_by_Segment():
        w = shapefile.Writer(shapefile.POLYLINE)
        
        field0 = 'SEGMENTID'
        field1 = 'STREET'
        field2 = 'DIRECTION'
        field3 = 'FR_ST'
        field4 = 'TO_ST'
        field5 = 'LENGTH'
        field6 = 'STR_HEAD'
        field7 = 'ST_LNG'
        field8 = 'ST_LAT'
        field9 = 'END_LNG'
        field10 = 'END_LAT'
        #field11 = 'CURR_SPD'
        #field12 = 'LAST_UPDT'
        
        w.field(field0, 'N', '5')
        w.field(field1, 'C')
        w.field(field2, 'C', '2')
        w.field(field3, 'C')
        w.field(field4, 'C')
        w.field(field5, 'N', '20', 2)
        w.field(field6, 'C', '1')
        w.field(field7, 'N', '20', 10)
        w.field(field8, 'N', '20', 10)
        w.field(field9, 'N', '20', 10)
        w.field(field10, 'N', '20', 10)
        #w.field(field11, 'N', '5')
        #w.field(field12, 'C')  
    
        return w

def setInitialValue(ttOutList, resultStr):
    for item in ttOutList:
        sLNG = float(item[7])
        sLAT = float(item[8])
        eLNG = float(item[9])
        eLAT = float(item[10])
        
        w.line(parts=[[[sLNG, sLAT], [eLNG, eLAT]]])
        
        w.record(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10])
    w.save(resultStr)   

def setInitialCSV(ttOutList, filepath):
    with open(filepath, 'wb') as output:
        fieldnames = ['SegmentID','speed','update']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for item in ttOutList:
            writer.writerow({'SegmentID' : item[0], 'speed': item[11], 'update' : item[12]})
         
def setAdditionalCSV(ttOutList, filepath):
    existFile = open(filepath, 'rb')
    readFile =  csv.reader(existFile)
    
    row0 = readFile.next()
    
    print(len(row0)/2)
    
    row0.append('speed'+str(len(row0)/2))
    row0.append('update'+str(len(row0)/2-1))
    print(row0)

    all=[]
    
    for item1 in readFile:
        for item2 in ttOutList:
            if item2[0] == item1[0]:
                item1.append(item2[11])
                item1.append(item2[12])
                break
        print(item1)
        all.append(item1)
    
    with open(filepath, 'wb') as output:
        fieldnames = row0
        writer = csv.writer(output, delimiter=',')
        
        writer.writerow(fieldnames)
        for item3 in all:
            writer.writerow(item3)
    

if __name__ == '__main__':
    
    ttOut = COD.TT_by_Segment() 
    
    w = setField_TT_by_Segment()
    
    setInitialValue(ttOut, 'result1')
    
    isInitial =2
    numOfTimes = 10
    timeInterval = 5
      
    if isInitial == 1:
        
        setInitialCSV(ttOut, 'speed.csv')
        
    else:
        numIndex = 0
        while True:
            ttOut = COD.TT_by_Segment()
            
            setAdditionalCSV(ttOut, 'speed.csv')
            numIndex+=1
            if numOfTimes > numIndex :
                time.sleep(timeInterval * 60)
            else:
                break
            
        
       