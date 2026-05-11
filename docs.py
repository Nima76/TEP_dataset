xmvs = {
    'xmv_1': {
        'name': 'D Feed Flow',
        'stream': 2,
        'base_case_valve_percent': 63.053,
        'low_limit': 0,
        'high_limit': 5811,
        'unit': 'kg/h'
    },
    'xmv_2': {
        'name': 'E Feed Flow',
        'stream': 3,
        'base_case_valve_percent': 53.980,
        'low_limit': 0,
        'high_limit': 8354,
        'unit': 'kg/h'
    },
    'xmv_3': {
        'name': 'A Feed Flow',
        'stream': 1,
        'base_case_valve_percent': 24.644,
        'low_limit': 0,
        'high_limit': 1.017,
        'unit': 'kscmh'
    },
    'xmv_4': {
        'name': 'A and C Feed Flow',
        'stream': 4,
        'base_case_valve_percent': 61.302,
        'low_limit': 0,
        'high_limit': 15.25,
        'unit': 'kscmh'
    },
    'xmv_5': {
        'name': 'Compressor Recycle Valve',
        'stream': None,
        'base_case_valve_percent': 22.210,
        'low_limit': 0,
        'high_limit': 100,
        'unit': '%'
    },
    'xmv_6': {
        'name': 'Purge Valve',
        'stream': 9,
        'base_case_valve_percent': 40.064,
        'low_limit': 0,
        'high_limit': 100,
        'unit': '%'
    },
    'xmv_7': {
        'name': 'Separator Pot Liquid Flow',
        'stream': 10,
        'base_case_valve_percent': 38.100,
        'low_limit': 0,
        'high_limit': 65.71,
        'unit': 'm3/h'
    },
    'xmv_8': {
        'name': 'Stripper Liquid Product Flow',
        'stream': 11,
        'base_case_valve_percent': 46.534,
        'low_limit': 0,
        'high_limit': 49.10,
        'unit': 'm3/h'
    },
    'xmv_9': {
        'name': 'Stripper Steam Valve',
        'stream': None,
        'base_case_valve_percent': 47.446,
        'low_limit': 0,
        'high_limit': 100,
        'unit': '%'
    },
    'xmv_10': {
        'name': 'Reactor Cooling Water Flow',
        'stream': None,
        'base_case_valve_percent': 41.106,
        'low_limit': 0,
        'high_limit': 227.1,
        'unit': 'm3/h'
    },
    'xmv_11': {
        'name': 'Condenser Cooling Water Flow',
        'stream': None,
        'base_case_valve_percent': 18.114,
        'low_limit': 0,
        'high_limit': 272.6,
        'unit': 'm3/h'
    },
    'xmv_12': {
        'name': 'Agitator Speed',
        'stream': None,
        'base_case_valve_percent': 50.000,
        'low_limit': 150,
        'high_limit': 250,
        'unit': 'rpm'
    }
}

xmeas = {
    'xmeas_1': {
        'name': 'A feed',
        'stream': 1,
        'base_case_value': 0.25052,
        'unit': 'kscmh'
    },
    'xmeas_2': {
        'name': 'D feed',
        'stream': 2,
        'base_case_value': 3664.0,
        'unit': 'kg/h'
    },
    'xmeas_3': {
        'name': 'E feed',
        'stream': 3,
        'base_case_value': 4509.3,
        'unit': 'kg/h'
    },
    'xmeas_4': {
        'name': 'A and C feed',
        'stream': 4,
        'base_case_value': 9.3477,
        'unit': 'kscmh'
    },
    'xmeas_5': {
        'name': 'Recycle flow',
        'stream': 8,
        'base_case_value': 26.902,
        'unit': 'kscmh'
    },
    'xmeas_6': {
        'name': 'Reactor feed rate',
        'stream': 6,
        'base_case_value': 42.339,
        'unit': 'kscmh'
    },
    'xmeas_7': {
        'name': 'Reactor pressure',
        'stream': None,
        'base_case_value': 2705.0,
        'unit': 'kPa gauge',
        'oonstraints': {
            "normal_low_limit" : None,
            "normal_high_limit": 2895,
            "low_limit_shut_down": None,
            "high_limit_shut_down": 3000,
            "unit": "kpa"
        }
    },
    'xmeas_8': {
        'name': 'Reactor level',
        'stream': None,
        'base_case_value': 75.000,
        'unit': '%',
        'oonstraints': {
            "normal_low_limit" : 11.8, # 50%
            "normal_high_limit": 21.3, # 100% 
            "low_limit_shut_down": 2.0*100/24, # 2.0 m3 converted to % of max capacity (21.3 m3)
            "high_limit_shut_down": 24.0*100/24, # 24.0 m3 converted to % of max capacity (21.3 m3)
            "unit": "m3"
        }
    },
    'xmeas_9': {
        'name': 'Reactor temperature',
        'stream': None,
        'base_case_value': 120.40,
        'unit': 'C',
        'oonstraints': {
            "normal_low_limit" : None,
            "normal_high_limit": 150,
            "low_limit_shut_down": None,
            "high_limit_shut_down": 175,
            "unit": "C"
        }
    },
    'xmeas_10': {
        'name': 'Purge rate',
        'stream': 9,
        'base_case_value': 0.33712,
        'unit': 'kscmh'
    },
    'xmeas_11': {
        'name': 'Product separator temperature',
        'stream': None,
        'base_case_value': 80.109,
        'unit': 'C'
    },
    'xmeas_12': {
        'name': 'Product separator level',
        'stream': None,
        'base_case_value': 50.000,
        'unit': '%',
        'oonstraints': {
            "normal_low_limit" : 3.3, # 30%
            "normal_high_limit": 9.0, # 100% 
            "low_limit_shut_down": 1,
            "high_limit_shut_down": 12,
            "unit": "m3"
        }
    },
    'xmeas_13': {
        'name': 'Product separator pressure',
        'stream': None,
        'base_case_value': 2633.7,
        'unit': 'kPa gauge'
    },
    'xmeas_14': {
        'name': 'Product separator underflow',
        'stream': 10,
        'base_case_value': 25.160,
        'unit': 'm3/h'
    },
    'xmeas_15': {
        'name': 'Stripper level',
        'stream': None,
        'base_case_value': 50.000,
        'unit': '%',
        'oonstraints': {
            "normal_low_limit" : 3.6, # 30%
            "normal_high_limit": 6.6, # 100% 
            "low_limit_shut_down": 1,
            "high_limit_shut_down": 8,
            "unit": "m3"
        }
    },
    'xmeas_16': {
        'name': 'Stripper pressure',
        'stream': None,
        'base_case_value': 3102.2,
        'unit': 'kPa gauge'
    },
    'xmeas_17': {
        'name': 'Stripper underflow',
        'stream': 11,
        'base_case_value': 22.949,
        'unit': 'm3/h'
    },
    'xmeas_18': {
        'name': 'Stripper temperature',
        'stream': None,
        'base_case_value': 65.731,
        'unit': 'C'
    },
    'xmeas_19': {
        'name': 'Stripper steam flow',
        'stream': None,
        'base_case_value': 230.31,
        'unit': 'kg/h'
    },
    'xmeas_20': {
        'name': 'Compressor work',
        'stream': None,
        'base_case_value': 341.43,
        'unit': 'kW'
    },
    'xmeas_21': {
        'name': 'Reactor cooling water outlet temperature',
        'stream': None,
        'base_case_value': 94.599,
        'unit': 'C'
    },
    'xmeas_22': {
        'name': 'Separator cooling water outlet temperature',
        'stream': None,
        'base_case_value': 77.297,
        'unit': 'C'
    },
    
    'xmeas_23': {'name': 'Reactor feed Component A', 'stream': 6, 'base_case_value': 32.188, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_24': {'name': 'Reactor feed Component B', 'stream': 6, 'base_case_value': 8.8933, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_25': {'name': 'Reactor feed Component C', 'stream': 6, 'base_case_value': 26.383, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_26': {'name': 'Reactor feed Component D', 'stream': 6, 'base_case_value': 6.8820, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_27': {'name': 'Reactor feed Component E', 'stream': 6, 'base_case_value': 18.776, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_28': {'name': 'Reactor feed Component F', 'stream': 6, 'base_case_value': 1.6567, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h

    'xmeas_29': {'name': 'Purge gas Component A', 'stream': 9, 'base_case_value': 32.958, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_30': {'name': 'Purge gas Component B', 'stream': 9, 'base_case_value': 13.823, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_31': {'name': 'Purge gas Component C', 'stream': 9, 'base_case_value': 23.978, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_32': {'name': 'Purge gas Component D', 'stream': 9, 'base_case_value': 1.2565, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_33': {'name': 'Purge gas Component E', 'stream': 9, 'base_case_value': 18.579, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_34': {'name': 'Purge gas Component F', 'stream': 9, 'base_case_value': 2.2633, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_35': {'name': 'Purge gas Component G', 'stream': 9, 'base_case_value': 4.8436, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_36': {'name': 'Purge gas Component H', 'stream': 9, 'base_case_value': 2.2986, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h

    'xmeas_37': {'name': 'Product Component D', 'stream': 11, 'base_case_value': 0.01787, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_38': {'name': 'Product Component E', 'stream': 11, 'base_case_value': 0.83570, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_39': {'name': 'Product Component F', 'stream': 11, 'base_case_value': 0.09858, 'unit': 'mol%'}, #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_40': {'name': 'Product Component G', 'stream': 11, 'base_case_value': 53.724, 'unit': 'mol%'},  #Sampling freq: 0.1 h, Dead time: 0.1 h
    'xmeas_41': {'name': 'Product Component H', 'stream': 11, 'base_case_value': 43.828, 'unit': 'mol%'},   #Sampling freq: 0.1 h, Dead time: 0.1 h

# Extra variables provided by revision
    'xmeas_42': {'name': 'Temperature A feed', 'stream': 1, 'base_case_value': 45, 'unit': 'C'},
    'xmeas_43': {'name': 'Temperature D feed', 'stream': 2, 'base_case_value': 45, 'unit': 'C'},
    'xmeas_44': {'name': 'Temperature E feed', 'stream': 3, 'base_case_value': 45, 'unit': 'C'},
    'xmeas_45': {'name': 'Temperature A and C feed', 'stream': 4, 'base_case_value': 45, 'unit': 'C'},
    'xmeas_46': {'name': 'Reactor cooling water inlet temperature', 'base_case_value': 35, 'unit': 'C'},
    'xmeas_47': {'name': 'Reactor cooling water flow', 'base_case_value': 93.37, 'unit': 'm3/h'},
    'xmeas_48': {'name': 'Condenser cooling water inlet temperature', 'base_case_value': 40, 'unit': 'C'},
    'xmeas_49': {'name': 'Condenser cooling water flow', 'base_case_value': 49.37, 'unit': 'm3/h'},
    'xmeas_50': {'name': 'Composition of A feed (stream 1); components A', 'unit': 'mol%'},
    'xmeas_51': {'name': 'Composition of A feed (stream 1); components B', 'unit': 'mol%'},
    'xmeas_52': {'name': 'Composition of A feed (stream 1); components C', 'unit': 'mol%'},
    'xmeas_53': {'name': 'Composition of A feed (stream 1); components D', 'unit': 'mol%'},
    'xmeas_54': {'name': 'Composition of A feed (stream 1); components E', 'unit': 'mol%'},
    'xmeas_55': {'name': 'Composition of A feed (stream 1); components F', 'unit': 'mol%'},
    'xmeas_56': {'name': 'Composition of D feed (stream 2); components A', 'unit': 'mol%'},
    'xmeas_57': {'name': 'Composition of D feed (stream 2); components B', 'unit': 'mol%'},
    'xmeas_58': {'name': 'Composition of D feed (stream 2); components C', 'unit': 'mol%'},
    'xmeas_59': {'name': 'Composition of D feed (stream 2); components D', 'unit': 'mol%'},
    'xmeas_60': {'name': 'Composition of D feed (stream 2); components E', 'unit': 'mol%'},
    'xmeas_61': {'name': 'Composition of D feed (stream 2); components F', 'unit': 'mol%'},
    'xmeas_62': {'name': 'Composition of E feed (stream 3); components A', 'unit': 'mol%'},
    'xmeas_63': {'name': 'Composition of E feed (stream 3); components B', 'unit': 'mol%'},
    'xmeas_64': {'name': 'Composition of E feed (stream 3); components C', 'unit': 'mol%'},
    'xmeas_65': {'name': 'Composition of E feed (stream 3); components D', 'unit': 'mol%'},
    'xmeas_66': {'name': 'Composition of E feed (stream 3); components E', 'unit': 'mol%'},
    'xmeas_67': {'name': 'Composition of E feed (stream 3); components F', 'unit': 'mol%'},
    'xmeas_68': {'name': 'Composition of A and C feed (stream 4); components A', 'unit': 'mol%'},
    'xmeas_69': {'name': 'Composition of A and C feed (stream 4); components B', 'unit': 'mol%'},
    'xmeas_70': {'name': 'Composition of A and C feed (stream 4); components C', 'unit': 'mol%'},
    'xmeas_71': {'name': 'Composition of A and C feed (stream 4); components D', 'unit': 'mol%'},
    'xmeas_72': {'name': 'Composition of A and C feed (stream 4); components E', 'unit': 'mol%'},
    'xmeas_73': {'name': 'Composition of A and C feed (stream 4); components F', 'unit': 'mol%'},
}

