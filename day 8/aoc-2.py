import copy

input = [
{'operation':'acc', 'amount': 0},
{'operation':'acc', 'amount': -11},
{'operation':'acc', 'amount': -19},
{'operation':'acc', 'amount': -18},
{'operation':'jmp', 'amount': +356},
{'operation':'nop', 'amount': +29},
{'operation':'acc', 'amount': +22},
{'operation':'jmp', 'amount': +619},
{'operation':'jmp', 'amount': +97},
{'operation':'acc', 'amount': -14},
{'operation':'jmp', 'amount': +71},
{'operation':'nop', 'amount': +54},
{'operation':'nop', 'amount': +348},
{'operation':'jmp', 'amount': +144},
{'operation':'jmp', 'amount': +123},
{'operation':'nop', 'amount': +27},
{'operation':'acc', 'amount': +48},
{'operation':'acc', 'amount': +3},
{'operation':'acc', 'amount': +2},
{'operation':'jmp', 'amount': +79},
{'operation':'jmp', 'amount': +576},
{'operation':'acc', 'amount': -7},
{'operation':'acc', 'amount': +37},
{'operation':'acc', 'amount': +37},
{'operation':'jmp', 'amount': +478},
{'operation':'acc', 'amount': +49},
{'operation':'nop', 'amount': +600},
{'operation':'acc', 'amount': +28},
{'operation':'jmp', 'amount': +388},
{'operation':'acc', 'amount': +6},
{'operation':'jmp', 'amount': +232},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +140},
{'operation':'acc', 'amount': +36},
{'operation':'acc', 'amount': -15},
{'operation':'acc', 'amount': +21},
{'operation':'acc', 'amount': +29},
{'operation':'jmp', 'amount': +361},
{'operation':'acc', 'amount': +4},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': +585},
{'operation':'acc', 'amount': +44},
{'operation':'acc', 'amount': -16},
{'operation':'acc', 'amount': +42},
{'operation':'acc', 'amount': -12},
{'operation':'jmp', 'amount': +252},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': +19},
{'operation':'acc', 'amount': +7},
{'operation':'acc', 'amount': +38},
{'operation':'jmp', 'amount': +232},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +26},
{'operation':'jmp', 'amount': +132},
{'operation':'acc', 'amount': +46},
{'operation':'acc', 'amount': -19},
{'operation':'jmp', 'amount': +219},
{'operation':'acc', 'amount': +45},
{'operation':'acc', 'amount': -1},
{'operation':'acc', 'amount': +23},
{'operation':'jmp', 'amount': +376},
{'operation':'acc', 'amount': +41},
{'operation':'nop', 'amount': +2},
{'operation':'jmp', 'amount': +55},
{'operation':'acc', 'amount': +24},
{'operation':'acc', 'amount': +43},
{'operation':'acc', 'amount': -3},
{'operation':'jmp', 'amount': -53},
{'operation':'acc', 'amount': +2},
{'operation':'acc', 'amount': +19},
{'operation':'jmp', 'amount': +520},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +9},
{'operation':'acc', 'amount': -2},
{'operation':'acc', 'amount': +40},
{'operation':'jmp', 'amount': +284},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': +250},
{'operation':'jmp', 'amount': +454},
{'operation':'jmp', 'amount': +559},
{'operation':'acc', 'amount': +22},
{'operation':'nop', 'amount': +561},
{'operation':'jmp', 'amount': +425},
{'operation':'jmp', 'amount': +146},
{'operation':'jmp', 'amount': +236},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +222},
{'operation':'acc', 'amount': -19},
{'operation':'acc', 'amount': -10},
{'operation':'acc', 'amount': -8},
{'operation':'jmp', 'amount': +399},
{'operation':'nop', 'amount': +410},
{'operation':'acc', 'amount': +49},
{'operation':'acc', 'amount': -1},
{'operation':'jmp', 'amount': +209},
{'operation':'jmp', 'amount': -88},
{'operation':'jmp', 'amount': +263},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': -5},
{'operation':'acc', 'amount': +31},
{'operation':'jmp', 'amount': +438},
{'operation':'acc', 'amount': -10},
{'operation':'acc', 'amount': +37},
{'operation':'jmp', 'amount': +404},
{'operation':'acc', 'amount': +34},
{'operation':'acc', 'amount': +49},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -79},
{'operation':'acc', 'amount': +23},
{'operation':'acc', 'amount': +0},
{'operation':'nop', 'amount': -23},
{'operation':'acc', 'amount': +47},
{'operation':'jmp', 'amount': -71},
{'operation':'jmp', 'amount': +277},
{'operation':'acc', 'amount': +37},
{'operation':'nop', 'amount': +144},
{'operation':'acc', 'amount': +16},
{'operation':'jmp', 'amount': +248},
{'operation':'nop', 'amount': +179},
{'operation':'jmp', 'amount': +413},
{'operation':'jmp', 'amount': +177},
{'operation':'acc', 'amount': +18},
{'operation':'acc', 'amount': +1},
{'operation':'acc', 'amount': +36},
{'operation':'acc', 'amount': -19},
{'operation':'jmp', 'amount': +145},
{'operation':'acc', 'amount': -8},
{'operation':'acc', 'amount': +34},
{'operation':'jmp', 'amount': +154},
{'operation':'nop', 'amount': +174},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': +272},
{'operation':'acc', 'amount': +46},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': +219},
{'operation':'acc', 'amount': -3},
{'operation':'acc', 'amount': +1},
{'operation':'nop', 'amount': -81},
{'operation':'jmp', 'amount': +335},
{'operation':'acc', 'amount': -4},
{'operation':'acc', 'amount': -18},
{'operation':'acc', 'amount': +11},
{'operation':'jmp', 'amount': +139},
{'operation':'nop', 'amount': +221},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +1},
{'operation':'jmp', 'amount': +295},
{'operation':'acc', 'amount': -4},
{'operation':'jmp', 'amount': +205},
{'operation':'jmp', 'amount': +270},
{'operation':'nop', 'amount': +87},
{'operation':'acc', 'amount': +11},
{'operation':'acc', 'amount': +37},
{'operation':'nop', 'amount': +61},
{'operation':'jmp', 'amount': +319},
{'operation':'acc', 'amount': +39},
{'operation':'acc', 'amount': -16},
{'operation':'jmp', 'amount': +327},
{'operation':'acc', 'amount': +34},
{'operation':'acc', 'amount': -14},
{'operation':'acc', 'amount': -5},
{'operation':'nop', 'amount': -142},
{'operation':'jmp', 'amount': +417},
{'operation':'jmp', 'amount': +1},
{'operation':'nop', 'amount': +467},
{'operation':'acc', 'amount': +7},
{'operation':'jmp', 'amount': -87},
{'operation':'nop', 'amount': +186},
{'operation':'nop', 'amount': +158},
{'operation':'acc', 'amount': +44},
{'operation':'jmp', 'amount': -157},
{'operation':'jmp', 'amount': +281},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +29},
{'operation':'acc', 'amount': +40},
{'operation':'jmp', 'amount': +132},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': -18},
{'operation':'jmp', 'amount': +345},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': +49},
{'operation':'jmp', 'amount': +9},
{'operation':'acc', 'amount': +30},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +261},
{'operation':'acc', 'amount': +38},
{'operation':'acc', 'amount': +42},
{'operation':'acc', 'amount': -6},
{'operation':'nop', 'amount': +369},
{'operation':'jmp', 'amount': +256},
{'operation':'nop', 'amount': -173},
{'operation':'jmp', 'amount': +6},
{'operation':'acc', 'amount': +44},
{'operation':'acc', 'amount': -4},
{'operation':'acc', 'amount': +46},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': +229},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +44},
{'operation':'acc', 'amount': +26},
{'operation':'jmp', 'amount': -74},
{'operation':'acc', 'amount': +25},
{'operation':'nop', 'amount': -55},
{'operation':'acc', 'amount': -15},
{'operation':'acc', 'amount': +24},
{'operation':'jmp', 'amount': -90},
{'operation':'acc', 'amount': +15},
{'operation':'jmp', 'amount': +214},
{'operation':'acc', 'amount': +48},
{'operation':'nop', 'amount': -35},
{'operation':'acc', 'amount': -1},
{'operation':'jmp', 'amount': +287},
{'operation':'jmp', 'amount': +249},
{'operation':'acc', 'amount': -11},
{'operation':'acc', 'amount': +36},
{'operation':'nop', 'amount': +407},
{'operation':'nop', 'amount': -75},
{'operation':'jmp', 'amount': +405},
{'operation':'acc', 'amount': -14},
{'operation':'acc', 'amount': +9},
{'operation':'acc', 'amount': -14},
{'operation':'jmp', 'amount': -204},
{'operation':'acc', 'amount': +34},
{'operation':'acc', 'amount': +31},
{'operation':'nop', 'amount': +171},
{'operation':'jmp', 'amount': +63},
{'operation':'acc', 'amount': +7},
{'operation':'acc', 'amount': +1},
{'operation':'acc', 'amount': +23},
{'operation':'jmp', 'amount': -222},
{'operation':'acc', 'amount': +17},
{'operation':'acc', 'amount': -13},
{'operation':'acc', 'amount': +13},
{'operation':'acc', 'amount': -6},
{'operation':'jmp', 'amount': +401},
{'operation':'acc', 'amount': +15},
{'operation':'acc', 'amount': -10},
{'operation':'acc', 'amount': +38},
{'operation':'jmp', 'amount': -146},
{'operation':'acc', 'amount': +9},
{'operation':'nop', 'amount': +155},
{'operation':'jmp', 'amount': -211},
{'operation':'acc', 'amount': -14},
{'operation':'acc', 'amount': +41},
{'operation':'nop', 'amount': +163},
{'operation':'acc', 'amount': -16},
{'operation':'jmp', 'amount': +54},
{'operation':'acc', 'amount': +3},
{'operation':'acc', 'amount': +1},
{'operation':'jmp', 'amount': -108},
{'operation':'acc', 'amount': +42},
{'operation':'nop', 'amount': -77},
{'operation':'acc', 'amount': -6},
{'operation':'jmp', 'amount': -27},
{'operation':'acc', 'amount': +12},
{'operation':'jmp', 'amount': +231},
{'operation':'jmp', 'amount': +321},
{'operation':'jmp', 'amount': -39},
{'operation':'acc', 'amount': +16},
{'operation':'acc', 'amount': +41},
{'operation':'acc', 'amount': +1},
{'operation':'jmp', 'amount': -114},
{'operation':'acc', 'amount': +10},
{'operation':'acc', 'amount': -2},
{'operation':'acc', 'amount': -18},
{'operation':'acc', 'amount': +7},
{'operation':'jmp', 'amount': +220},
{'operation':'jmp', 'amount': +103},
{'operation':'nop', 'amount': +144},
{'operation':'acc', 'amount': +39},
{'operation':'nop', 'amount': -186},
{'operation':'jmp', 'amount': +85},
{'operation':'acc', 'amount': -17},
{'operation':'acc', 'amount': +5},
{'operation':'acc', 'amount': +36},
{'operation':'acc', 'amount': -14},
{'operation':'jmp', 'amount': +369},
{'operation':'acc', 'amount': +3},
{'operation':'jmp', 'amount': +101},
{'operation':'jmp', 'amount': +38},
{'operation':'acc', 'amount': +16},
{'operation':'acc', 'amount': +16},
{'operation':'acc', 'amount': +49},
{'operation':'acc', 'amount': +35},
{'operation':'jmp', 'amount': +169},
{'operation':'jmp', 'amount': +190},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': -226},
{'operation':'acc', 'amount': +15},
{'operation':'jmp', 'amount': -83},
{'operation':'acc', 'amount': -2},
{'operation':'acc', 'amount': -1},
{'operation':'acc', 'amount': +11},
{'operation':'jmp', 'amount': -175},
{'operation':'nop', 'amount': +305},
{'operation':'acc', 'amount': +12},
{'operation':'acc', 'amount': +34},
{'operation':'nop', 'amount': +153},
{'operation':'jmp', 'amount': +294},
{'operation':'jmp', 'amount': -189},
{'operation':'acc', 'amount': +8},
{'operation':'jmp', 'amount': +334},
{'operation':'acc', 'amount': +23},
{'operation':'acc', 'amount': +48},
{'operation':'jmp', 'amount': +146},
{'operation':'jmp', 'amount': -63},
{'operation':'nop', 'amount': +329},
{'operation':'acc', 'amount': +25},
{'operation':'nop', 'amount': -3},
{'operation':'acc', 'amount': +4},
{'operation':'jmp', 'amount': -209},
{'operation':'acc', 'amount': +39},
{'operation':'acc', 'amount': +30},
{'operation':'acc', 'amount': +22},
{'operation':'acc', 'amount': +35},
{'operation':'jmp', 'amount': +292},
{'operation':'jmp', 'amount': +29},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +48},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': +92},
{'operation':'acc', 'amount': +25},
{'operation':'acc', 'amount': +3},
{'operation':'jmp', 'amount': +72},
{'operation':'nop', 'amount': +180},
{'operation':'acc', 'amount': +7},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +18},
{'operation':'jmp', 'amount': -159},
{'operation':'jmp', 'amount': +181},
{'operation':'acc', 'amount': +15},
{'operation':'jmp', 'amount': -46},
{'operation':'acc', 'amount': -7},
{'operation':'acc', 'amount': +46},
{'operation':'acc', 'amount': +25},
{'operation':'jmp', 'amount': +252},
{'operation':'acc', 'amount': -2},
{'operation':'acc', 'amount': +50},
{'operation':'acc', 'amount': +24},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': -272},
{'operation':'acc', 'amount': +20},
{'operation':'acc', 'amount': +38},
{'operation':'acc', 'amount': -17},
{'operation':'jmp', 'amount': +12},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': +136},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +32},
{'operation':'acc', 'amount': +50},
{'operation':'jmp', 'amount': -83},
{'operation':'acc', 'amount': +35},
{'operation':'acc', 'amount': -10},
{'operation':'jmp', 'amount': -118},
{'operation':'acc', 'amount': +4},
{'operation':'jmp', 'amount': -325},
{'operation':'jmp', 'amount': +136},
{'operation':'acc', 'amount': -5},
{'operation':'nop', 'amount': +164},
{'operation':'acc', 'amount': -8},
{'operation':'acc', 'amount': -8},
{'operation':'jmp', 'amount': +174},
{'operation':'jmp', 'amount': -38},
{'operation':'jmp', 'amount': +108},
{'operation':'nop', 'amount': -8},
{'operation':'acc', 'amount': +8},
{'operation':'jmp', 'amount': +196},
{'operation':'nop', 'amount': -234},
{'operation':'acc', 'amount': +47},
{'operation':'jmp', 'amount': +260},
{'operation':'acc', 'amount': +31},
{'operation':'acc', 'amount': +26},
{'operation':'acc', 'amount': -8},
{'operation':'jmp', 'amount': +96},
{'operation':'acc', 'amount': +0},
{'operation':'nop', 'amount': -294},
{'operation':'acc', 'amount': +3},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -330},
{'operation':'nop', 'amount': +1},
{'operation':'acc', 'amount': +32},
{'operation':'acc', 'amount': +36},
{'operation':'jmp', 'amount': +160},
{'operation':'nop', 'amount': -201},
{'operation':'acc', 'amount': +24},
{'operation':'acc', 'amount': +48},
{'operation':'jmp', 'amount': -114},
{'operation':'acc', 'amount': +32},
{'operation':'nop', 'amount': +251},
{'operation':'jmp', 'amount': +233},
{'operation':'acc', 'amount': +22},
{'operation':'nop', 'amount': -330},
{'operation':'acc', 'amount': +8},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +67},
{'operation':'nop', 'amount': +115},
{'operation':'nop', 'amount': -304},
{'operation':'jmp', 'amount': +171},
{'operation':'acc', 'amount': +2},
{'operation':'acc', 'amount': +7},
{'operation':'jmp', 'amount': -55},
{'operation':'nop', 'amount': +186},
{'operation':'jmp', 'amount': +214},
{'operation':'acc', 'amount': +12},
{'operation':'nop', 'amount': -148},
{'operation':'nop', 'amount': -388},
{'operation':'jmp', 'amount': -232},
{'operation':'acc', 'amount': -11},
{'operation':'acc', 'amount': +1},
{'operation':'jmp', 'amount': -98},
{'operation':'acc', 'amount': +39},
{'operation':'jmp', 'amount': -250},
{'operation':'jmp', 'amount': -337},
{'operation':'nop', 'amount': -388},
{'operation':'acc', 'amount': +49},
{'operation':'acc', 'amount': +45},
{'operation':'jmp', 'amount': -54},
{'operation':'acc', 'amount': +17},
{'operation':'acc', 'amount': -8},
{'operation':'jmp', 'amount': -57},
{'operation':'jmp', 'amount': +209},
{'operation':'jmp', 'amount': -231},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': -124},
{'operation':'acc', 'amount': +49},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +45},
{'operation':'jmp', 'amount': -84},
{'operation':'acc', 'amount': +3},
{'operation':'acc', 'amount': -3},
{'operation':'jmp', 'amount': -402},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': -8},
{'operation':'acc', 'amount': -7},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': -30},
{'operation':'jmp', 'amount': +54},
{'operation':'acc', 'amount': +2},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': +75},
{'operation':'nop', 'amount': -224},
{'operation':'acc', 'amount': +16},
{'operation':'jmp', 'amount': -270},
{'operation':'acc', 'amount': +43},
{'operation':'acc', 'amount': +34},
{'operation':'jmp', 'amount': -68},
{'operation':'acc', 'amount': +45},
{'operation':'jmp', 'amount': -4},
{'operation':'acc', 'amount': +23},
{'operation':'jmp', 'amount': -421},
{'operation':'jmp', 'amount': -152},
{'operation':'acc', 'amount': +47},
{'operation':'acc', 'amount': -19},
{'operation':'jmp', 'amount': -361},
{'operation':'jmp', 'amount': -259},
{'operation':'acc', 'amount': +20},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -187},
{'operation':'jmp', 'amount': -188},
{'operation':'nop', 'amount': +10},
{'operation':'nop', 'amount': -368},
{'operation':'acc', 'amount': -5},
{'operation':'jmp', 'amount': -403},
{'operation':'acc', 'amount': +45},
{'operation':'acc', 'amount': -12},
{'operation':'nop', 'amount': -357},
{'operation':'jmp', 'amount': -51},
{'operation':'jmp', 'amount': -139},
{'operation':'jmp', 'amount': -258},
{'operation':'nop', 'amount': -464},
{'operation':'acc', 'amount': +49},
{'operation':'jmp', 'amount': +37},
{'operation':'jmp', 'amount': -359},
{'operation':'acc', 'amount': +30},
{'operation':'jmp', 'amount': -315},
{'operation':'acc', 'amount': -9},
{'operation':'acc', 'amount': +5},
{'operation':'acc', 'amount': +28},
{'operation':'acc', 'amount': +5},
{'operation':'jmp', 'amount': -187},
{'operation':'acc', 'amount': -9},
{'operation':'acc', 'amount': +47},
{'operation':'jmp', 'amount': -133},
{'operation':'jmp', 'amount': +50},
{'operation':'acc', 'amount': +19},
{'operation':'acc', 'amount': +8},
{'operation':'jmp', 'amount': -81},
{'operation':'acc', 'amount': -3},
{'operation':'acc', 'amount': +18},
{'operation':'jmp', 'amount': -265},
{'operation':'nop', 'amount': -53},
{'operation':'jmp', 'amount': +1},
{'operation':'jmp', 'amount': -164},
{'operation':'acc', 'amount': +44},
{'operation':'nop', 'amount': -322},
{'operation':'jmp', 'amount': -76},
{'operation':'acc', 'amount': -17},
{'operation':'acc', 'amount': +42},
{'operation':'acc', 'amount': +8},
{'operation':'acc', 'amount': +2},
{'operation':'jmp', 'amount': -421},
{'operation':'jmp', 'amount': -285},
{'operation':'acc', 'amount': +41},
{'operation':'acc', 'amount': -2},
{'operation':'jmp', 'amount': +133},
{'operation':'acc', 'amount': +13},
{'operation':'nop', 'amount': -47},
{'operation':'jmp', 'amount': -340},
{'operation':'acc', 'amount': +40},
{'operation':'acc', 'amount': -16},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': +13},
{'operation':'jmp', 'amount': +115},
{'operation':'jmp', 'amount': +77},
{'operation':'acc', 'amount': -10},
{'operation':'acc', 'amount': -9},
{'operation':'acc', 'amount': -16},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': -264},
{'operation':'jmp', 'amount': -126},
{'operation':'acc', 'amount': +49},
{'operation':'jmp', 'amount': -98},
{'operation':'acc', 'amount': +26},
{'operation':'acc', 'amount': -19},
{'operation':'acc', 'amount': +24},
{'operation':'acc', 'amount': +34},
{'operation':'jmp', 'amount': -338},
{'operation':'acc', 'amount': +13},
{'operation':'jmp', 'amount': -242},
{'operation':'acc', 'amount': +7},
{'operation':'acc', 'amount': -5},
{'operation':'nop', 'amount': -233},
{'operation':'jmp', 'amount': -234},
{'operation':'acc', 'amount': -12},
{'operation':'acc', 'amount': +4},
{'operation':'jmp', 'amount': +62},
{'operation':'acc', 'amount': +9},
{'operation':'nop', 'amount': -485},
{'operation':'acc', 'amount': +9},
{'operation':'jmp', 'amount': -236},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': -16},
{'operation':'acc', 'amount': +20},
{'operation':'nop', 'amount': -497},
{'operation':'jmp', 'amount': +11},
{'operation':'acc', 'amount': +41},
{'operation':'acc', 'amount': +8},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': +49},
{'operation':'jmp', 'amount': -172},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': +23},
{'operation':'jmp', 'amount': -501},
{'operation':'jmp', 'amount': -495},
{'operation':'nop', 'amount': -285},
{'operation':'acc', 'amount': +22},
{'operation':'acc', 'amount': +36},
{'operation':'jmp', 'amount': -103},
{'operation':'jmp', 'amount': -513},
{'operation':'acc', 'amount': +0},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -480},
{'operation':'nop', 'amount': -254},
{'operation':'acc', 'amount': +31},
{'operation':'jmp', 'amount': -96},
{'operation':'acc', 'amount': +9},
{'operation':'acc', 'amount': +18},
{'operation':'acc', 'amount': +27},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -431},
{'operation':'acc', 'amount': +34},
{'operation':'acc', 'amount': +31},
{'operation':'nop', 'amount': -104},
{'operation':'jmp', 'amount': -66},
{'operation':'acc', 'amount': -5},
{'operation':'acc', 'amount': +30},
{'operation':'acc', 'amount': +21},
{'operation':'nop', 'amount': -362},
{'operation':'jmp', 'amount': -471},
{'operation':'acc', 'amount': +7},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +47},
{'operation':'nop', 'amount': -184},
{'operation':'jmp', 'amount': -561},
{'operation':'acc', 'amount': -1},
{'operation':'jmp', 'amount': -36},
{'operation':'acc', 'amount': +42},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': -306},
{'operation':'acc', 'amount': +3},
{'operation':'acc', 'amount': -11},
{'operation':'acc', 'amount': +15},
{'operation':'acc', 'amount': +40},
{'operation':'jmp', 'amount': -481},
{'operation':'acc', 'amount': +30},
{'operation':'jmp', 'amount': -537},
{'operation':'acc', 'amount': +45},
{'operation':'nop', 'amount': -358},
{'operation':'jmp', 'amount': -322},
{'operation':'nop', 'amount': -169},
{'operation':'nop', 'amount': -298},
{'operation':'acc', 'amount': +14},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': +23},
{'operation':'acc', 'amount': -14},
{'operation':'acc', 'amount': +43},
{'operation':'nop', 'amount': -111},
{'operation':'jmp', 'amount': -492},
{'operation':'acc', 'amount': +43},
{'operation':'acc', 'amount': +19},
{'operation':'acc', 'amount': +44},
{'operation':'acc', 'amount': +9},
{'operation':'jmp', 'amount': -365},
{'operation':'acc', 'amount': +25},
{'operation':'acc', 'amount': +24},
{'operation':'acc', 'amount': +5},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -256},
{'operation':'jmp', 'amount': -488},
{'operation':'acc', 'amount': +17},
{'operation':'jmp', 'amount': -170},
{'operation':'nop', 'amount': -17},
{'operation':'acc', 'amount': +50},
{'operation':'acc', 'amount': +5},
{'operation':'nop', 'amount': -494},
{'operation':'jmp', 'amount': -292},
{'operation':'jmp', 'amount': -234},
{'operation':'acc', 'amount': +42},
{'operation':'acc', 'amount': -1},
{'operation':'nop', 'amount': -365},
{'operation':'acc', 'amount': -15},
{'operation':'jmp', 'amount': -47},
{'operation':'jmp', 'amount': +1},
{'operation':'acc', 'amount': -9},
{'operation':'jmp', 'amount': -286},
{'operation':'jmp', 'amount': -523},
{'operation':'acc', 'amount': -13},
{'operation':'acc', 'amount': +1},
{'operation':'acc', 'amount': +27},
{'operation':'acc', 'amount': +0},
{'operation':'jmp', 'amount': -393},
{'operation':'jmp', 'amount': -327},
{'operation':'acc', 'amount': -4},
{'operation':'acc', 'amount': +37},
{'operation':'nop', 'amount': -375},
{'operation':'acc', 'amount': +38},
{'operation':'jmp', 'amount': +1}
]

def detectLoop(program):
    hitInstructions = []
    index = 0
    accumulator = 0

    while index not in hitInstructions and index < len(program):
        hitInstructions.append(index)
        command = program[index]

        op = command['operation']
        value = command['amount']

        indexIncrease = 1
        if op == 'jmp':
            indexIncrease = value

        elif op == 'acc':
            accumulator += value

        index += indexIncrease

    return {
            'accumulator': accumulator,
            'loopDetected': index < len(program) - 1
           }

permutableOps = []
for i, instruction in enumerate(input):
    if instruction['operation'] == 'nop' or instruction['operation'] == 'jmp':
        permutableOps.append(i)

print('Permutable op indexes: {}'.format(permutableOps))

for i in permutableOps:
    print('Permuting OP {}'.format(i))
    permutedInput = copy.deepcopy(input)

    if(permutedInput[i]['operation'] == 'nop'):
        permutedInput[i]['operation'] = 'jmp'

    elif(permutedInput[i]['operation'] == 'jmp'):
        permutedInput[i]['operation'] = 'nop'

    result = detectLoop(permutedInput)
    if not result['loopDetected']:
        print('Program terminated. Accumulator: {}'.format(result['accumulator']))
        break
