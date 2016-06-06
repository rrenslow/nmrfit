

class Experiment:
    def __init__(self, name):
        if name == "dc-0445_cdcl3_kilimanjaro_22c_1d_1H_1_031816.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2661462618751593, 3.2694674160474411], 125.91502],
                            [[3.2987539573848355, 3.3023770346636883], 133.51155],
                            [[3.5336501342971318, 3.5375751346825561], 113.77483],
                            [[3.5668616760199505, 3.5698809070856612], 110.23856]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0028984618230822878, 3.4359757426313995, 0.0032755301424847055,
                                      0.002101384821734653, 3.4031468181787705, 0.0031777329196757782,
                                      0.0028984618230822878, 3.5681908630296593, 1.5488772569912292e-05,
                                      0.0028984618230822878, 3.5353619385770303, 1.7830132352995666e-05,
                                      0.0028984618230822878, 3.3006126431760383, 1.2280666906327427e-05,
                                      0.0028984618230822878, 3.2677837187234093, 1.2686546791932418e-05]
        elif name == "dc-0445_cdcl3_kilimanjaro_22c_1d_1H_2_031816.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2655424156620172, 3.2694674160474411], 121.52854],
                            [[3.2984520342782644, 3.3023770346636883], 131.97],
                            [[3.5333482111905608, 3.5378770577891272], 109.90247],
                            [[3.5668616760199505, 3.5704847532988033], 108.49534]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0026267310271683277, 3.4359757426313995, 0.0032589849433525015,
                                      0.0021738463673117272, 3.4031468181787705, 0.0032243269126972546,
                                      0.0026267310271683277, 3.5677411517357878, 1.6678226629129063e-05,
                                      0.0026267310271683277, 3.5353619385770303, 1.4590805182842432e-05,
                                      0.0026267310271683277, 3.3001629318821668, 1.4183764583088661e-05,
                                      0.0026267310271683277, 3.2677837187234093, 1.4246493557187728e-05]

        elif name == "dc-0445_cdcl3_kilimanjaro_22c_1d_1H_3_031816.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2658443387685883, 3.2697693391540121], 125.11756],
                            [[3.2984520342782644, 3.3023770346636883], 125.07958],
                            [[3.5339520574037033, 3.5372732115759851], 107.20149],
                            [[3.5662578298068084, 3.5698809070856612], 107.71215]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0023912310040429042, 3.435526031337528, 0.0032608547844216679,
                                      0.0023550002312544118, 3.4031468181787705, 0.0032371447258201492,
                                      0.0023912310040429042, 3.5677411517357878, 1.5412621549916679e-05,
                                      0.0023912310040429042, 3.5353619385770303, 1.3598731571871046e-05,
                                      0.0023912310040429042, 3.3001629318821668, 1.2997687084800013e-05,
                                      0.0023912310040429042, 3.2677837187234093, 1.4323134531937849e-05]

        elif name == "dc-0445_cdcl3_kilimanjaro_25c_1d_1H_1_032716.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2570885686780269, 3.2607116459568797], 117.90932],
                            [[3.2903001104008451, 3.2939231876796979], 114.90696],
                            [[3.525498210419713, 3.5291212876985658], 115.0295],
                            [[3.5578039828228181, 3.5617289832082419], 121.88363]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0019564617305805497, 3.4269815167539668, 0.0029130113689093385,
                                      0.0019564617305805497, 3.3946023035952093, 0.00292000992977188,
                                      0.0019564617305805497, 3.5596463484460985, 1.333900753842446e-05,
                                      0.0019564617305805497, 3.5268174239934691, 1.4361148351092141e-05,
                                      0.0019564617305805497, 3.2916184172986056, 1.4143589003389837e-05,
                                      0.0019564617305805497, 3.2592392041398481, 1.2927519350780982e-05]

        elif name == "dc-0445_cdcl3_kilimanjaro_25c_1d_1H_2_032716.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2570885686780269, 3.2607116459568797], 122.20083],
                            [[3.2903001104008451, 3.2933193414665558], 115.53181],
                            [[3.5248943642065709, 3.5282155183788526], 112.03566],
                            [[3.557502059716247, 3.5608232138885287], 115.21027]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0020651540489461605, 3.4265318054600953, 0.0029104856048341641,
                                      0.0017390770938493726, 3.3941525923013378, 0.0029018757707570428,
                                      0.0020651540489461605, 3.5591966371522266, 1.4872398906156685e-05,
                                      0.0020651540489461605, 3.5263677126995976, 1.5553329601682615e-05,
                                      0.0020651540489461605, 3.2911687060047341, 1.2615208343291572e-05,
                                      0.0020651540489461605, 3.2587894928459766, 1.4327708072996237e-05]

        elif name == "dc-919V_cdcl3_kilimanjaro_25c_1d_1H_1_031916.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2749020319657203, 3.2776193399248599], 123.298],
                            [[3.3081135736885385, 3.310227035434536], 122.81613],
                            [[3.5418020581745511, 3.5454251354534039], 134.81677],
                            [[3.5750135998973693, 3.5783347540696511], 133.21709]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0023550002312543671, 3.4440705459210887, 0.0027943867095681797,
                                      0.0021738463673117272, 3.4116913327623313, 0.0028096177030071008,
                                      0.0023550002312543671, 3.5762856663193485, 1.2937477125675833e-05,
                                      0.0023550002312543671, 3.5439064531605911, 1.3454691734487678e-05,
                                      0.0023550002312543671, 3.3087074464657276, 1.2414476686288132e-05,
                                      0.0023550002312543671, 3.2758785220130986, 1.2906443116754046e-05]

        elif name == "dc-919V_cdcl3_kilimanjaro_25c_1d_1H_1_032616.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2688635698342989, 3.2724866471131517], 131.61722],
                            [[3.301169342237404, 3.3053962657293989], 135.93791],
                            [[3.5363674422562719, 3.5405943657482668], 109.91167],
                            [[3.5695789839790901, 3.5729001381513719], 110.73409]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0021376155945231901, 3.4386740103946294, 0.0029009552856041915,
                                      0.0018840001850034759, 3.4058450859420004, 0.002860337428099565,
                                      0.0021376155945231901, 3.5708891307928892, 1.488968117478962e-05,
                                      0.0021376155945231901, 3.5380602063402602, 1.6092146534360761e-05,
                                      0.0021376155945231901, 3.3033109109392682, 1.1780022092216065e-05,
                                      0.0021376155945231901, 3.2704819864866392, 1.1933605542440241e-05]

        elif name == "dc-919V_cdcl3_kilimanjaro_25c_1d_1H_2_031916.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2742981857525781, 3.2773174168182888], 125.67613],
                            [[3.3063020350491121, 3.3105289585411071], 124.81045],
                            [[3.5418020581745511, 3.5457270585599749], 128.44527],
                            [[3.5744097536842272, 3.5777309078565089], 134.68298]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0021013848217346976, 3.4436208346272172, 0.0027148488165654439,
                                      0.0018840001850035204, 3.4112416214684598, 0.0027010495453065882,
                                      0.0021013848217346976, 3.575835955025477, 1.2325321532826175e-05,
                                      0.0021013848217346976, 3.5434567418667196, 1.3837053690142389e-05,
                                      0.0021013848217346976, 3.3082577351718561, 1.236099940625024e-05,
                                      0.0021013848217346976, 3.2758785220130986, 1.2949608002553493e-05]

        elif name == "dc-919V_cdcl3_kilimanjaro_25c_1d_1H_2_032616.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2685616467277279, 3.2718828009000096], 130.28073],
                            [[3.301169342237404, 3.3044904964096857], 143.40793],
                            [[3.5360655191497008, 3.5399905195351247], 107.92912],
                            [[3.5695789839790901, 3.5729001381513719], 107.23183]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0030796156870249282, 3.4382242991007579, 0.0029261766702347787,
                                      0.0024274617768314409, 3.4053953746481285, 0.002858660179467599,
                                      0.0030796156870249282, 3.5704394194990172, 1.6123043768278127e-05,
                                      0.0030796156870249282, 3.5376104950463882, 1.6777669139544411e-05,
                                      0.0030796156870249282, 3.3028611996453967, 1.1071394923201012e-05,
                                      0.0030796156870249282, 3.2700322751927673, 1.1741226834031577e-05]

        elif name == "dc-919V_cdcl3_kilimanjaro_25c_1d_1H_3_031916.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2727885702197228, 3.2770154937117177], 129.60632],
                            [[3.3063020350491121, 3.3099251123279649], 124.26025],
                            [[3.5408962888548379, 3.5445193661336907], 121.13961],
                            [[3.5741078305776561, 3.5774289847499379], 127.74224]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0023912310040429484, 3.4431711233333457, 0.0027317589822509823,
                                      0.0024274617768314409, 3.4107919101745883, 0.0027219106395100206,
                                      0.0023912310040429484, 3.575835955025477, 1.210906704986822e-05,
                                      0.0023912310040429484, 3.543007030572848, 1.2602142447672279e-05,
                                      0.0023912310040429484, 3.3078080238779846, 1.0439065359606449e-05,
                                      0.0023912310040429484, 3.2754288107192271, 1.2272743585975976e-05]

        elif name == "dc-070_cdcl3_kilimanjaro_25c_1d_1H_1_032016.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.264636646342304, 3.26916549294087], 130.3364],
                            [[3.2972443418519801, 3.3023770346636883], 128.33615],
                            [[3.5327443649774186, 3.5375751346825561], 107.54688],
                            [[3.5650501373805237, 3.5698809070856612], 108.30618]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0023550002312543671, 3.4350763200436565, 0.0028930814786310762,
                                      0.0021738463673117272, 3.402697106884899, 0.0028745514513895789,
                                      0.0023550002312543671, 3.5672914404419158, 1.4688255465925146e-05,
                                      0.0023550002312543671, 3.5349122272831583, 1.5783985616176231e-05,
                                      0.0023550002312543671, 3.2997132205882953, 1.0721622371236126e-05,
                                      0.0023550002312543671, 3.2673340074295378, 1.257093969381482e-05]

        elif name == "dc-070_cdcl3_kilimanjaro_25c_1d_1H_1_032716.fid":
            '!!!'
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2585981842108822, 3.2613154921700218], 118.96727],
                            [[3.2906020335074162, 3.294225110786269], 119.49821],
                            [[3.525498210419713, 3.5291212876985658], 124.13959],
                            [[3.5584078290359602, 3.5617289832082419], 132.23541]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0020832694353404512, 3.3948929766186691, -0.0028646761491951237,
                                      0.0020832694353404512, 3.4276465413985502, -0.0028525834106832132,
                                      0.0020832694353404512, 3.2594789849167771, -1.0459684581390679e-05,
                                      0.0020832694353404512, 3.2922325496966565, -1.3590532009581937e-05,
                                      0.0020832694353404512, 3.5273738132656476, -1.3374012217991909e-05,
                                      0.0020832694353404512, 3.5596385188697077, -1.3132883069053288e-05]

        elif name == "dc-070_cdcl3_kilimanjaro_25c_1d_1H_2_032016.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.264636646342304, 3.26916549294087], 127.53656],
                            [[3.2963385725322669, 3.3014712653439751], 134.01822],
                            [[3.5324424418708475, 3.5366693653628429], 110.30609],
                            [[3.5647482142739526, 3.5692770608725191], 109.59437]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0019202309577920572, 3.4346266087497845, 0.0028681176875402776,
                                      0.0019564617305805497, 3.4022473955910271, 0.0028600990705031251,
                                      0.0019202309577920572, 3.5668417291480443, 1.3879735106886636e-05,
                                      0.0019202309577920572, 3.5344625159892868, 1.5126705137566771e-05,
                                      0.0019202309577920572, 3.2992635092944234, 1.1900265955427653e-05,
                                      0.0019202309577920572, 3.2668842961356659, 1.0685281411679575e-05]

        elif name == "dc-070_cdcl3_kilimanjaro_25c_1d_1H_2_032716.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2567866455714558, 3.2613154921700218], 124.29002],
                            [[3.2899981872942741, 3.2939231876796979], 121.53413],
                            [[3.5251962873131419, 3.5291212876985658], 120.41637],
                            [[3.5568982135031049, 3.5623328294213841], 124.72375]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0021013848217346976, 3.4269815167539668, 0.0028221835200333764,
                                      0.0018115386394264466, 3.3946023035952093, 0.0028130867641109635,
                                      0.0021013848217346976, 3.5596463484460985, 1.4419710100776437e-05,
                                      0.0021013848217346976, 3.5268174239934691, 1.3771827857788022e-05,
                                      0.0021013848217346976, 3.2916184172986056, 1.3042210294580847e-05,
                                      0.0021013848217346976, 3.2592392041398481, 1.0702469873883415e-05]

        elif name == "dc-070_cdcl3_kilimanjaro_25c_1d_1H_3_032016.fid":
            self.weights = [['all', 1.0],
                            ['all', 1.0],
                            [[3.2640328001291619, 3.2682597236211568], 130.2469],
                            [[3.2972443418519801, 3.3008674191308329], 137.59071],
                            [[3.5321405187642765, 3.5360655191497008], 112.48838],
                            [[3.5641443680608105, 3.568975137765948], 112.11996]]

            self.initialConditions = [0, 0.1, 0,
                                      0.0020832694353404512, 3.4017370050801361, -0.0028434715181920606,
                                      0.0021436540566546203, 3.434001710684198, -0.0028767389697132708,
                                      0.0020832694353404512, 3.2663230133782442, -1.2702963112195327e-05,
                                      0.0020832694353404512, 3.2985877189823043, -1.1572618245732872e-05,
                                      0.0020832694353404512, 3.5337289825512954, -1.5823713781010799e-05,
                                      0.0020832694353404512, 3.5664825473311765, -1.6798041800114565e-05]

        else:
            print("Error")
