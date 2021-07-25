#!/usr/bin/python

import pandas as pd
import numpy as np
import pickle
import sys
import os

def predict_price(year,mileage,state,make,model):

    """# clf =  pickle.load(open(os.path.dirname(__file__) + '/phishing_clf.pkl', 'rb'))
    # clf =  pickle.load(open(os.path.dirname(__file__) + '/API' +'/phishing_clf.pkl', 'rb'))
    # clf = pickle.load(open('./phishing_clf.pkl', 'rb'))"""
        
    clf = pickle.load(open('API/phishing_clf.pkl', 'rb'))
    #clf = pickle.load(open('./phishing_clf.pkl', 'rb'))

    list_part_a = ['Make_Audi','Make_BMW','Make_Bentley','Make_Buick','Make_Cadillac','Make_Chevrolet','Make_Chrysler','Make_Dodge','Make_FIAT','Make_Ford','Make_Freightliner','Make_GMC','Make_Honda','Make_Hyundai','Make_INFINITI','Make_Jaguar','Make_Jeep','Make_Kia','Make_Land','Make_Lexus','Make_Lincoln','Make_MINI','Make_Mazda','Make_Mercedes-Benz','Make_Mercury','Make_Mitsubishi','Make_Nissan','Make_Pontiac','Make_Porsche','Make_Ram','Make_Scion','Make_Subaru','Make_Suzuki','Make_Tesla','Make_Toyota','Make_Volkswagen','Make_Volvo','Mileage']
    
    list_part_b = ['Model_15002WD','Model_15004WD','Model_1500Laramie','Model_1500Tradesman','Model_200LX','Model_200Limited','Model_200S','Model_200Touring','Model_25002WD','Model_25004WD','Model_3','Model_300300C','Model_300300S','Model_3004dr','Model_300Base','Model_300Limited','Model_300Touring','Model_35004WD','Model_350Z2dr','Model_4Runner2WD','Model_4Runner4WD','Model_4Runner4dr','Model_4RunnerLimited','Model_4RunnerRWD','Model_4RunnerSR5','Model_4RunnerTrail','Model_5','Model_500Pop','Model_6','Model_7','Model_911','Model_9112dr','Model_A34dr','Model_A44dr','Model_A64dr','Model_A8','Model_AcadiaAWD','Model_AcadiaFWD','Model_Accent4dr','Model_Accord','Model_AccordEX','Model_AccordEX-L','Model_AccordLX','Model_AccordLX-S','Model_AccordSE','Model_Altima4dr','Model_Armada2WD','Model_Armada4WD','Model_Avalanche2WD','Model_Avalanche4WD','Model_Avalon4dr','Model_AvalonLimited','Model_AvalonTouring','Model_AvalonXLE','Model_Azera4dr','Model_Boxster2dr','Model_C-Class4dr','Model_C-ClassC','Model_C-ClassC300','Model_C-ClassC350','Model_C702dr','Model_CC4dr','Model_CR-V2WD','Model_CR-V4WD','Model_CR-VEX','Model_CR-VEX-L','Model_CR-VLX','Model_CR-VSE','Model_CR-ZEX','Model_CT','Model_CTCT','Model_CTS','Model_CTS-V','Model_CTS4dr','Model_CX-7FWD','Model_CX-9AWD','Model_CX-9FWD','Model_CX-9Grand','Model_CX-9Touring','Model_Caliber4dr','Model_Camaro2dr','Model_CamaroConvertible','Model_CamaroCoupe','Model_Camry','Model_Camry4dr','Model_CamryBase','Model_CamryL','Model_CamryLE','Model_CamrySE','Model_CamryXLE','Model_Canyon2WD','Model_Canyon4WD','Model_CanyonCrew','Model_CanyonExtended','Model_CayenneAWD','Model_Cayman2dr','Model_Challenger2dr','Model_ChallengerR/T','Model_Charger4dr','Model_ChargerSE','Model_ChargerSXT','Model_CherokeeLimited','Model_CherokeeSport','Model_Civic','Model_CivicEX','Model_CivicEX-L','Model_CivicLX','Model_CivicSi','Model_Cobalt2dr','Model_Cobalt4dr','Model_Colorado2WD','Model_Colorado4WD','Model_ColoradoCrew','Model_ColoradoExtended','Model_Compass4WD','Model_CompassLatitude','Model_CompassLimited','Model_CompassSport','Model_Continental','Model_Cooper','Model_Corolla4dr','Model_CorollaL','Model_CorollaLE','Model_CorollaS','Model_Corvette2dr','Model_CorvetteConvertible','Model_CorvetteCoupe','Model_CruzeLT','Model_CruzeSedan','Model_DTS4dr','Model_Dakota2WD','Model_Dakota4WD','Model_Durango2WD','Model_Durango4dr','Model_DurangoAWD','Model_DurangoSXT','Model_E-ClassE','Model_E-ClassE320','Model_E-ClassE350','Model_ES','Model_ESES','Model_Eclipse3dr','Model_Econoline','Model_EdgeLimited','Model_EdgeSE','Model_EdgeSEL','Model_EdgeSport','Model_Elantra','Model_Elantra4dr','Model_ElantraLimited','Model_Element2WD','Model_Element4WD','Model_EnclaveConvenience','Model_EnclaveLeather','Model_EnclavePremium','Model_Eos2dr','Model_EquinoxAWD','Model_EquinoxFWD','Model_Escalade','Model_Escalade2WD','Model_Escalade4dr','Model_EscaladeAWD','Model_Escape4WD','Model_Escape4dr','Model_EscapeFWD','Model_EscapeLImited','Model_EscapeLimited','Model_EscapeS','Model_EscapeSE','Model_EscapeXLT','Model_Excursion137"','Model_Expedition','Model_Expedition2WD','Model_Expedition4WD','Model_ExpeditionLimited','Model_ExpeditionXLT','Model_Explorer','Model_Explorer4WD','Model_Explorer4dr','Model_ExplorerBase','Model_ExplorerEddie','Model_ExplorerFWD','Model_ExplorerLimited','Model_ExplorerXLT','Model_Express','Model_F-1502WD','Model_F-1504WD','Model_F-150FX2','Model_F-150FX4','Model_F-150King','Model_F-150Lariat','Model_F-150Limited','Model_F-150Platinum','Model_F-150STX','Model_F-150SuperCrew','Model_F-150XL','Model_F-150XLT','Model_F-250King','Model_F-250Lariat','Model_F-250XL','Model_F-250XLT','Model_F-350King','Model_F-350Lariat','Model_F-350XL','Model_F-350XLT','Model_FJ','Model_FX35AWD','Model_FiestaS','Model_FiestaSE','Model_FitSport','Model_FlexLimited','Model_FlexSE','Model_FlexSEL','Model_Focus4dr','Model_Focus5dr','Model_FocusS','Model_FocusSE','Model_FocusSEL','Model_FocusST','Model_FocusTitanium','Model_Forester2.5X','Model_Forester4dr','Model_Forte','Model_ForteEX','Model_ForteLX','Model_ForteSX','Model_Frontier','Model_Frontier2WD','Model_Frontier4WD','Model_Fusion4dr','Model_FusionHybrid','Model_FusionS','Model_FusionSE','Model_FusionSEL','Model_G35','Model_G37','Model_G64dr','Model_GLI4dr','Model_GS','Model_GSGS','Model_GTI2dr','Model_GTI4dr','Model_GX','Model_GXGX','Model_Galant4dr','Model_Genesis','Model_Golf','Model_Grand','Model_Highlander','Model_Highlander4WD','Model_Highlander4dr','Model_HighlanderBase','Model_HighlanderFWD','Model_HighlanderLimited','Model_HighlanderSE','Model_IS','Model_ISIS','Model_Impala4dr','Model_ImpalaLS','Model_ImpalaLT','Model_Impreza','Model_Impreza2.0i','Model_ImprezaSport','Model_Jetta','Model_JourneyAWD','Model_JourneyFWD','Model_JourneySXT','Model_LS','Model_LSLS','Model_LX','Model_LXLX','Model_LaCrosse4dr','Model_LaCrosseAWD','Model_LaCrosseFWD','Model_Lancer4dr','Model_Land','Model_Legacy','Model_Legacy2.5i','Model_Legacy3.6R','Model_Liberty4WD','Model_LibertyLimited','Model_LibertySport','Model_Lucerne4dr','Model_M-ClassML350','Model_MDX4WD','Model_MDXAWD','Model_MKXAWD','Model_MKXFWD','Model_MKZ4dr','Model_MX5','Model_Malibu','Model_Malibu1LT','Model_Malibu4dr','Model_MalibuLS','Model_MalibuLT','Model_Matrix5dr','Model_Maxima4dr','Model_Mazda34dr','Model_Mazda35dr','Model_Mazda64dr','Model_Milan4dr','Model_Model','Model_Monte','Model_Murano2WD','Model_MuranoAWD','Model_MuranoS','Model_Mustang2dr','Model_MustangBase','Model_MustangDeluxe','Model_MustangGT','Model_MustangPremium','Model_MustangShelby','Model_Navigator','Model_Navigator2WD','Model_Navigator4WD','Model_Navigator4dr','Model_New','Model_OdysseyEX','Model_OdysseyEX-L','Model_OdysseyLX','Model_OdysseyTouring','Model_Optima4dr','Model_OptimaEX','Model_OptimaLX','Model_OptimaSX','Model_Outback2.5i','Model_Outback3.6R','Model_Outlander','Model_Outlander2WD','Model_Outlander4WD','Model_PT','Model_PacificaLimited','Model_PacificaTouring','Model_Passat','Model_Passat4dr','Model_Pathfinder2WD','Model_Pathfinder4WD','Model_PathfinderS','Model_PathfinderSE','Model_Patriot4WD','Model_PatriotLatitude','Model_PatriotLimited','Model_PatriotSport','Model_Pilot2WD','Model_Pilot4WD','Model_PilotEX','Model_PilotEX-L','Model_PilotLX','Model_PilotSE','Model_PilotTouring','Model_Prius','Model_Prius5dr','Model_PriusBase','Model_PriusFive','Model_PriusFour','Model_PriusOne','Model_PriusThree','Model_PriusTwo','Model_Q5quattro','Model_Q7quattro','Model_QX562WD','Model_QX564WD','Model_Quest4dr','Model_RAV4','Model_RAV44WD','Model_RAV44dr','Model_RAV4Base','Model_RAV4FWD','Model_RAV4LE','Model_RAV4Limited','Model_RAV4Sport','Model_RAV4XLE','Model_RDXAWD','Model_RDXFWD','Model_RX','Model_RX-84dr','Model_RXRX','Model_Ram','Model_Ranger2WD','Model_Ranger4WD','Model_RangerSuperCab','Model_Regal4dr','Model_RegalGS','Model_RegalPremium','Model_RegalTurbo','Model_RidgelineRTL','Model_RidgelineSport','Model_RioLX','Model_RogueFWD','Model_Rover','Model_S2000Manual','Model_S44dr','Model_S60T5','Model_S804dr','Model_SC','Model_SL-ClassSL500','Model_SLK-ClassSLK350','Model_SRXLuxury','Model_STS4dr','Model_Santa','Model_Savana','Model_Sedona4dr','Model_SedonaEX','Model_SedonaLX','Model_Sentra4dr','Model_Sequoia4WD','Model_Sequoia4dr','Model_SequoiaLimited','Model_SequoiaPlatinum','Model_SequoiaSR5','Model_Sienna5dr','Model_SiennaLE','Model_SiennaLimited','Model_SiennaSE','Model_SiennaXLE','Model_Sierra','Model_Silverado','Model_Sonata4dr','Model_SonataLimited','Model_SonataSE','Model_SonicHatch','Model_SonicSedan','Model_Sorento2WD','Model_SorentoEX','Model_SorentoLX','Model_SorentoSX','Model_Soul+','Model_SoulBase','Model_Sportage2WD','Model_SportageAWD','Model_SportageEX','Model_SportageLX','Model_SportageSX','Model_Sprinter','Model_Suburban2WD','Model_Suburban4WD','Model_Suburban4dr','Model_Super','Model_TL4dr','Model_TLAutomatic','Model_TSXAutomatic','Model_TT2dr','Model_Tacoma2WD','Model_Tacoma4WD','Model_TacomaBase','Model_TacomaPreRunner','Model_Tahoe2WD','Model_Tahoe4WD','Model_Tahoe4dr','Model_TahoeLS','Model_TahoeLT','Model_Taurus4dr','Model_TaurusLimited','Model_TaurusSE','Model_TaurusSEL','Model_TaurusSHO','Model_TerrainAWD','Model_TerrainFWD','Model_Tiguan2WD','Model_TiguanS','Model_TiguanSE','Model_TiguanSEL','Model_Titan','Model_Titan2WD','Model_Titan4WD','Model_Touareg4dr','Model_Town','Model_Transit','Model_TraverseAWD','Model_TraverseFWD','Model_TucsonAWD','Model_TucsonFWD','Model_TucsonLimited','Model_Tundra','Model_Tundra2WD','Model_Tundra4WD','Model_TundraBase','Model_TundraLimited','Model_TundraSR5','Model_VeracruzAWD','Model_VeracruzFWD','Model_Versa4dr','Model_Versa5dr','Model_Vibe4dr','Model_WRXBase','Model_WRXLimited','Model_WRXPremium','Model_WRXSTI','Model_Wrangler','Model_Wrangler2dr','Model_Wrangler4WD','Model_WranglerRubicon','Model_WranglerSahara','Model_WranglerSport','Model_WranglerX','Model_X1xDrive28i','Model_X3AWD','Model_X3xDrive28i','Model_X5AWD','Model_X5xDrive35i','Model_XC60AWD','Model_XC60FWD','Model_XC60T6','Model_XC704dr','Model_XC90AWD','Model_XC90FWD','Model_XC90T6','Model_XF4dr','Model_XJ4dr','Model_XK2dr','Model_Xterra2WD','Model_Xterra4WD','Model_Xterra4dr','Model_Yaris','Model_Yaris4dr','Model_YarisBase','Model_YarisLE','Model_Yukon','Model_Yukon2WD','Model_Yukon4WD','Model_Yukon4dr','Model_tC2dr','Model_xB5dr','Model_xD5dr']
    
    list_part_c = ['State_ AL','State_ AR','State_ AZ','State_ CA','State_ CO','State_ CT','State_ DC','State_ DE','State_ FL','State_ GA','State_ HI','State_ IA','State_ ID','State_ IL','State_ IN','State_ KS','State_ KY','State_ LA','State_ MA','State_ MD','State_ ME','State_ MI','State_ MN','State_ MO','State_ MS','State_ MT','State_ NC','State_ ND','State_ NE','State_ NH','State_ NJ','State_ NM','State_ NV','State_ NY','State_ OH','State_ OK','State_ OR','State_ PA','State_ RI','State_ SC','State_ SD','State_ TN','State_ TX','State_ UT','State_ VA','State_ VT','State_ WA','State_ WI','State_ WV','State_ WY','Year']
    
    list_ = list_part_a + list_part_b + list_part_c
    
    """list_ = ['Year','Mileage','Model_Silverado','Make_GMC','Model_Super','Make_Land','Make_Lexus','Model_F-1504WD','Make_BMW','Make_Mercedes-Benz','Model_Wrangler','Model_Tahoe4WD','Model_Suburban4WD','Model_Escalade','Make_Kia','Make_Ram','Model_Suburban2WD','Model_Tundra','Model_Tahoe2WD','Model_TahoeLT','Model_TerrainFWD','Model_Sierra','Model_FusionSE','Model_CorvetteCoupe','Make_Ford','Model_Grand','Model_FocusSE','Make_Porsche','Make_Dodge','Model_25004WD','Make_Cadillac','Make_Volkswagen','Model_F-150Lariat','Model_F-250Lariat','Model_CorollaLE','Model_CruzeSedan','Make_Lincoln','Model_EscapeSE','Make_Nissan','Model_F-150SuperCrew','Model_TerrainAWD','State_ TX','Make_Tesla','Make_Jeep','Make_Hyundai','Model_CayenneAWD','State_ FL','Model_Tacoma4WD','State_ CA','Model_3','Model_Land','Model_F-350Lariat','Model_4Runner4WD','Model_MalibuLT','Model_TundraSR5','Model_MDXAWD','Model_Yukon']"""
    
    """list_ = ['Year','Mileage','Model_Silverado','Make_GMC','Model_Super','Make_Land','Make_Lexus','Model_F-1504WD','Make_BMW','Make_Mercedes-Benz','Model_Wrangler','Model_Tahoe4WD','Model_Suburban4WD','Model_Escalade','Make_Kia','Make_Ram','Model_Suburban2WD','Model_Tundra','Model_Tahoe2WD','Model_TahoeLT','Model_TerrainFWD','Model_Sierra','Model_FusionSE','Model_CorvetteCoupe','Make_Ford','Model_Grand','Model_FocusSE']"""

    # Create features
    estimacion = pd.DataFrame(np.zeros((1,613)),columns=list_)  
    
    estimacion['Year'] = year
    estimacion['Mileage'] = mileage    
    state = 'State_ ' + state
    estimacion['%s'%state] = 1 
    make = 'Make_' + make
    estimacion['%s'%make] = 1    
    model = 'Model_' + model
    estimacion['%s'%model] = 1

    # Make prediction
    p1 = clf.predict(estimacion)
    p1 = str(p1)

    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add parameters')
        
    else:     
        
        year = sys.argv[1]
        mileage = sys.argv[2]
        state = sys.argv[3]
        make = sys.argv[4]
        model = sys.argv[5]

        p1 = predict_price(year,mileage,state,make,model)
        
        print('Year: ',year)
        print('Mileage: ',mileage)
        print('State: ',state)
        print('Make: ',make)
        print('Model: ',model)
        
        print('Estimated Price of Car: ', p1)
        