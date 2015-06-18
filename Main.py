'''
Created on Jun 18, 2015

@author: Bumsub
'''
import Web.APIs.ChicagoOpendata.ChicagoAPI as COD
import shapefile

if __name__ == '__main__':
    
    ttOut = COD.TT_by_Segment() 
    
    w = shapefile.Writer(shapefile.POLYLINE)
    
    
    '''
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
    field11 = 'CURR_SPD'
    field12 = 'LAST_UPDT'
    '''
    
    w.field('SEGMENTID', 'N', '5')
    w.field('STREET', 'C')
    w.field('DIRECTION', 'C', '2')
    w.field('FR_ST', 'C')
    w.field('TO_ST', 'C')
    w.field('LENGTH', 'N', '20', 2)
    w.field('STR_HEAD', 'C', '1')
    w.field('ST_LNG', 'N', '20', 10)
    w.field('ST_LAT', 'N', '20', 10)
    w.field('END_LNG', 'N', '20', 10)
    w.field('END_LAT', 'N', '20', 10)
    w.field('CURR_SPD', 'N', '5')
    w.field('LAST_UPDT', 'C')
       
        
    print(len(ttOut))    
    
    for item in ttOut:
        
        sLNG = float(item[7])
        sLAT = float(item[8])
        eLNG = float(item[9])
        eLAT = float(item[10])
        
        w.line(parts=[[[sLNG, sLAT], [eLNG, eLAT]]])
        
        w.record(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12])
        
    w.save('result')
    
        