from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, random

w,h= 1000,700
directionikan = random.choice([-1, 1])  
xikan = random.randrange(-2200, -100, 10)  
yikan = random.randrange(0, 1000, 10)
speedikan = 1



def ikan(radius, center=(217.6511054984415, 173.4093554967788)):
    global xikan,yikan,run_game,directionikan
    glPushMatrix()
    glTranslated(xikan,yikan,0)
    glScaled(0.15,0.15,0)

    xikan += speedikan * directionikan 

    if xikan < -100 or xikan > w + 100:
        yikan = random.randrange(0, h, 10)
        xikan = -100 if directionikan == 1 else w + 100  
        directionikan *= random.choice([-1, 1]) 
        # print(xapel, ' ikan)

    glColor3ub(186, 135, 89)
    glBegin(GL_POLYGON)
    glVertex2f(157.9974479688327, 274.2829524518862)
    glVertex2f(157.9777957341989, 242.9027256790382)
    glVertex2f(158.0765007283849, 241.3498267409983)
    glVertex2f(158.1149029545706, 239.6601287888246)
    glVertex2f(158, 238)
    glVertex2f(158.2685118593137, 236.2807328844773)
    glVertex2f(158.2301096331279, 234.4758282537464)
    glVertex2f(158.2685118593137, 231.9796835516717)
    glVertex2f(158.4605229902425, 230.4051922780553)
    glVertex2f(158.6525341211713, 228.984309909182)
    glVertex2f(158.8061430259144, 227.3714164093799)
    glVertex2f(159.190165287772, 225.2208917429771)
    glVertex2f(159.4589808710724, 223.6464004693607)
    glVertex2f(159.6125897758155, 221.9951047433728)
    glVertex2f(160, 220)
    glVertex2f(160.5182474520663, 217.0354220487228)
    glVertex2f(161.3011374330384, 213.4506100305874)
    glVertex2f(161.6958266417491, 210.9297546453529)
    glVertex2f(162.2707663876682, 208.6818473668157)
    glVertex2f(162.5965697210236, 207.1781396744063)
    glVertex2f(163.4486707467222, 204.0704771100938)
    glVertex2f(164.0000302339389, 202.5667694176845)
    glVertex2f(164.4762043365352, 200.7121965970463)
    glVertex2f(164.9523784391315, 199.258612494384)
    glVertex2f(165.2079000820469, 198.247958180367)
    glVertex2f(165.8020249531331, 196.5623015693783)
    glVertex2f(166.4376003966206, 194.5864909515801)
    glVertex2f(167.1837106998451, 192.6383140487162)
    glVertex2f(167.7358358503608, 191.0627083748617)
    glVertex2f(168.1540804795185, 190.2171268419994)
    glVertex2f(168.4359409904726, 189.2897148382149)
    glVertex2f(169.1905997778659, 187.5712749488495)
    glVertex2f(169.7017655995351, 186.4014884336131)
    glVertex2f(170.1106636976605, 185.481467712831)
    glVertex2f(170.4088185608769, 184.8084895929996)
    glVertex2f(170.9319258913987, 183.5273129042659)
    glVertex2f(171.6359239521707, 182.2037965500144)
    glVertex2f(172.1052559926854, 180.9366000406246)
    glVertex2f(172.7375964111708, 179.6308515306157)
    glVertex2f(173.0159355085166, 178.8364253569413)
    glVertex2f(173.7638812866113, 177.4201948027864)
    glVertex2f(174.6722578909974, 175.9002966934866)
    glVertex2f(175.4840525936003, 174.3105371293761)
    glVertex2f(176.3123679535656, 172.7253205518169)
    glVertex2f(177.0321510163437, 171.5328441343786)
    glVertex2f(177.8056492330604, 170.0825349780347)
    glVertex2f(179.062583835225, 168.1380464054551)
    glVertex2f(179.8824093869208, 166.595880229933)
    glVertex2f(180.6786628529989, 165.4770068250128)
    glVertex2f(181.0823945351514, 164.8087147959141)
    glVertex2f(181.7309469802256, 163.7371933649219)
    glVertex2f(182.5110897764743, 162.628074690737)
    glVertex2f(183.5299589929452, 161.1440541886041)
    glVertex2f(184.1070289978015, 160.2505264391493)
    glVertex2f(184.8144051327865, 158.928849976414)
    glVertex2f(185.6520873979004, 158.0167070655122)
    glVertex2f(186.2477725642035, 157.1976399618452)
    glVertex2f(187.0438615104147, 156.1704402154064)
    glVertex2f(187.7921205848236, 155.0820633799025)
    glVertex2f(188.5630541766388, 154.0390355792113)
    glVertex2f(189.2886387336413, 153.0867058481454)
    glVertex2f(190.2, 152)
    glVertex2f(191.1026001261477, 150.8419286249186)
    glVertex2f(192.1229534094325, 149.572155650164)
    glVertex2f(193.18865572753, 148.4611042972538)
    glVertex2f(193.7555186626882, 147.5994726358132)
    glVertex2f(194.843895498192, 146.5110958003094)
    glVertex2f(195.894050518285, 145.2675673162342)
    glVertex2f(196.9327415455029, 143.9692035322118)
    glVertex2f(197.9714325727207, 142.8266434022721)
    glVertex2f(199.08802542698, 141.7100505480128)
    glVertex2f(200.0488146271565, 140.7232940721557)
    glVertex2f(200.9317020002917, 139.7625048719791)
    glVertex2f(201.9184584761486, 138.7757483961221)
    glVertex2f(201.9184584761486, 138.7757483961221)
    glVertex2f(203.1389204331296, 137.6851228175432)
    glVertex2f(204.4905482161394, 136.3276607380342)
    glVertex2f(205.3975051441899, 135.535670181145)
    glVertex2f(206.8065907836728, 134.2836644158414)
    glVertex2f(208.334862863944, 132.8414921710783)
    glVertex2f(209.9277098208463, 131.4638948029464)
    glVertex2f(211.0039577646993, 130.5813714889869)
    glVertex2f(211.9, 129.8)
    glVertex2f(213.5223779533152, 128.4719255190349)
    glVertex2f(215.6748738410211, 126.7929787266241)
    glVertex2f(217.704953370355, 125.1784222576082)
    glVertex2f(218.9390350505558, 124.1500208574408)#L5 GARIS TENGAH KEPALA
    glVertex2f(221.3065932267011, 124.4208072416474)#O20
    glVertex2f(223.5436443775119, 124.6552758085959)
    glVertex2f(225.8875069300142, 124.965492911133)
    glVertex2f(227.955620946928, 125.3791157145158)
    glVertex2f(230, 126)
    glVertex2f(232.2641918154983, 126.8612640933042)
    glVertex2f(234.1311531014663, 127.6345803320513)
    glVertex2f(236.434115424502, 128.5886542796281)
    glVertex2f(238.2918927781418, 129.4360614935692)
    glVertex2f(239.8889294505691, 130.1508761223588)
    glVertex2f(241.4843408336784, 130.8354160204675)
    glVertex2f(243.4632642016192, 131.8794617122975)
    glVertex2f(245.8687944233344, 133.2299348192255)
    glVertex2f(248.3165269296411, 134.6648124953365)
    glVertex2f(250.4266411592159, 136.0996901714475)
    glVertex2f(252.7899690963396, 137.9565906934735)
    glVertex2f(255.4065107410123, 139.518075223359)
    glVertex2f(257.516624970587, 141.1639643224274)
    glVertex2f(259.7955483385277, 143.1896739828194)
    glVertex2f(262.0744717064684, 145.3841927815774)
    glVertex2f(264.1845859360432, 147.1144864498289)
    glVertex2f(265.872677319703, 149.0557915410379)
    glVertex2f(267.7717801263203, 151.3769171935704)
    glVertex2f(269.488679359232, 153.4828475752574)
    glVertex2f(271.4988609556652, 156.2796219702952)
    glVertex2f(273.916905484708, 159.5716584977876)
    glVertex2f(275.40949086785, 162.2764989286829)
    glVertex2f(277.3055851581261, 165.4072592684415)
    glVertex2f(278.5843464236611, 168.0088770155649)
    glVertex2f(279.7308220410374, 170.1695426021588)
    glVertex2f(280.9213928744665, 172.6829699171763)
    glVertex2f(281.891487627631, 174.8436355037702)
    glVertex2f(282.6852015165838, 176.8720154422054)
    glVertex2f(283.4348201894836, 179.1649666769581)
    glVertex2f(283.8757723500129, 181.413822695658)
    glVertex2f(284.339548138739, 183.3077938329918)
    glVertex2f(284.748713104447, 185.2172303396293)
    glVertex2f(285.4306547139603, 187.3994434900722)
    glVertex2f(285.66933427729, 189.377074157661)
    glVertex2f(285.8398196796683, 191.2865106642985)
    glVertex2f(285.976208001571, 193.6392092171197)
    glVertex2f(286.283081725852, 196.196490252795)
    glVertex2f(286.386433210016, 197.877090369461)
    glVertex2f(286.386433210016, 200.6501269143631)
    glVertex2f(286.1810230955789, 203.3204584020465)
    glVertex2f(286.1810230955789, 206.0934949469485)
    glVertex2f(285.8729079239232, 208.7638264346319)
    glVertex2f(285.5647927522674, 211.5368629795339)
    glVertex2f(285.0512674661745, 213.7450217097337)
    glVertex2f(284.6917997659095, 216.4667057260264)
    glVertex2f(283.7674542509423, 219.2910947995378)
    glVertex2f(283.2539289648494, 221.5506060583468)
    glVertex2f(282.6376986215379, 223.7587647885466)
    glVertex2f(282.5969830430009, 225.8133249342029)
    glVertex2f(282.3238292755912, 227.7689624354407)
    glVertex2f(281.9111137862676, 231.4244424837353)
    glVertex2f(280.9088047407676, 234.5787680092799)
    glVertex2f(279.6116989171793, 237.5267357901627)
    glVertex2f(278.314593093591, 240.887419060369)
    glVertex2f(277.6169005419681, 242.5777934413492)#I13 GARIS TENGAH KEPALA

    glVertex2f(274.5179562696327, 244.373772508271)#H13
    glVertex2f(270.9612134116114, 246.2753974026588)
    glVertex2f(268, 248)
    glVertex2f(264, 250)
    glVertex2f(261.5706669695792, 251.2866544969083)
    glVertex2f(258.5876108143644, 252.8240757461346)
    glVertex2f(255.0997297713439, 254.568016267645)
    glVertex2f(251.7495282431796, 255.8989182445872)
    glVertex2f(247.986288170447, 257.4822326654321)
    glVertex2f(244.796712742948, 258.6984017133275)
    glVertex2f(240.0509993118608, 260.7862615254639)
    glVertex2f(235.6714760033734, 262.4158515937385)
    glVertex2f(230.8845551778174, 263.8926675931123)
    glVertex2f(226.1994837315286, 265.2676342132189)
    glVertex2f(220.1903703547669, 266.8972242814934)
    glVertex2f(214.4868051158065, 268.3231155912337)
    glVertex2f(210.6165287036549, 269.2906846942717)
    glVertex2f(207.1027251189383, 270.0545550387754)
    glVertex2f(203.3132800810436, 270.6634571887858)
    glVertex2f(199.6995964311821, 271.2416465727637)
    glVertex2f(195.0258989106944, 271.8680184054064)
    glVertex2f(190.0149242495531, 272.6389375840436)
    glVertex2f(185.4375916263951, 273.3134918653512)
    glVertex2f(180.5711643112482, 273.650769006005)
    glVertex2f(176, 274)
    glVertex2f(170.6455798862951, 274.180775941318)
    glVertex2f(166.4055244037909, 274.3253232873125)
    glVertex2f(157.9974479688327, 274.2829524518862) #C
    glEnd()


    #BODY
    glColor3ub(186, 135, 89)
    glBegin(GL_POLYGON)
    glVertex2f(340.5396977050059, 95.8978484726309) #V7 BODY AWAL
    glVertex2f(346.1019852733443, 96.4152705720113)
    glVertex2f(352.2679319576264, 97.1914037210818)
    glVertex2f(355.5449385870351, 97.7950628370256)
    glVertex2f(359.1237747744156, 98.5280774778144)
    glVertex2f(365.5915510166695, 100.3821733339274)
    glVertex2f(371.4125496346981, 101.8050841072234)
    glVertex2f(377.3629037775718, 103.5298244384913)
    glVertex2f(383.9994952033156, 106.4557254832343)
    glVertex2f(389.4366726169483, 108.9550731653077)
    glVertex2f(395.5315731048108, 111.9805993067648)
    glVertex2f(399.2586705254462, 113.997616734403)
    glVertex2f(402.5911341015436, 116.0584823669898)
    glVertex2f(405.7482048578465, 117.9001069748333)
    glVertex2f(408.8175792042521, 119.6978833777281)
    glVertex2f(413.5093371337577, 123.2934361835178)
    glVertex2f(417.6991711276522, 126.3750794491119)
    glVertex2f(420.9318547064236, 128.9465322958621)
    glVertex2f(423.650247715845, 131.4077800206088)
    glVertex2f(428.5360081246698, 136.3670105107699)
    glVertex2f(431.8054267441091, 139.7098992115452)
    glVertex2f(434.891170160209, 142.905847749649)
    glVertex2f(436.7185536903968, 144.8211429386491) #L9 ekor awal 1
    glVertex2f(436.7655002837649, 184.8867614553629)
    glVertex2f(398.6606835772675, 184.2154128643619) #S16 ekor awal 2
    glVertex2f(396.2542532504609, 183.2147190650957)
    glVertex2f(393.9972739915936, 182.3579777162925)
    glVertex2f(388.4058739676095, 180.7167209928343)
    glVertex2f(385.5128112686327, 180.0769090497913)
    glVertex2f(381.7852112526433, 179.6040045701508)
    glVertex2f(378.5026978057272, 179.4370971067482)
    glVertex2f(373.0503873345786, 179.4092791961811)
    glVertex2f(368.65058027878, 179.6817399108076)
    glVertex2f(364.5704178296991, 180.0547833347236) #F16
    glVertex2f(362.7052007101192, 180.3811963306501)
    glVertex2f(360.5135705946129, 180.8941310385346)
    glVertex2f(358.92813604297, 181.3371201044348)
    glVertex2f(356.9230276394217, 181.9433156682983)
    glVertex2f(354.9878648778576, 182.5261960181671)
    glVertex2f(352.0734631285141, 183.6453262899151)
    glVertex2f(349.7901238494823, 184.6332745753594)
    glVertex2f(347.5235594478957, 185.5530398397715)
    glVertex2f(345.2569950463091, 186.8669902175029)
    glVertex2f(344.1401372252374, 187.4911166469254)
    glVertex2f(342.7933380880628, 188.1480918357912)
    glVertex2f(341.4793877103314, 188.9693108218733)
    glVertex2f(339.6070084220642, 190.4803537562646)
    glVertex2f(337.9, 191.8)
    glVertex2f(336.3221324777358, 193.0754057522842)
    glVertex2f(334.6796945055716, 194.5535999272322)
    glVertex2f(332.9715590145208, 196.2617354182831)
    glVertex2f(332.0189449906656, 197.3457444799116)
    glVertex2f(331.1320284856969, 198.1341147065505)
    glVertex2f(328.8269141317595, 200.4437134949577)
    glVertex2f(326.1122809396918, 203.2055576990617)
    glVertex2f(323.7223089625532, 205.619588426749)
    glVertex2f(321.3679898405556, 207.8584997486489)
    glVertex2f(320.2600749596156, 208.8740883895107)
    glVertex2f(318.2058161178726, 210.9745103512931)
    glVertex2f(316.1074524786724, 212.957723087029)
    glVertex2f(314.696380650715, 214.3165329954326)
    glVertex2f(313.5466184205275, 215.4924261853973)
    glVertex2f(312.0310227534621, 216.7989741742468)
    glVertex2f(310.4109032472888, 218.2361769619814)
    glVertex2f(308.8953075802234, 219.542724950831)
    glVertex2f(307.0661403958342, 221.2151063765585)
    glVertex2f(306, 222)
    glVertex2f(304.8471019140287, 223.0407968456766)
    glVertex2f(303.4984996800379, 224.1384963384599)
    glVertex2f(302.0558089180943, 225.2361958312432)
    glVertex2f(300.6444809988017, 226.3966210093284)
    glVertex2f(299.1704273942071, 227.7452232433193)
    glVertex2f(297.7904623175654, 228.7174713654988)
    glVertex2f(296, 230)
    glVertex2f(294.1523725700554, 231.4460386761315)
    glVertex2f(292.3960533816023, 232.7319152248205)
    glVertex2f(290.3261057666398, 234.2059688294152)
    glVertex2f(288.4984207709638, 235.3586618978399)
    glVertex2f(285.8572750843144, 237.2602867922277)
    glVertex2f(283.1456988460209, 238.9858353075056)
    glVertex2f(280.4341226077275, 240.8874602018934)
    glVertex2f(277.6169005419681, 242.5777934413492) #I13
    glVertex2f(218.9390350505558, 124.1500208574408)#L5 BODY
    glVertex2f(220.4816371508068, 123.1730395272817)
    glVertex2f(222, 122)
    glVertex2f(223.7725216313423, 120.9105564469133)
    glVertex2f(225.6750642216518, 119.5479245916915)
    glVertex2f(227.526186741953, 118.3652629814989)
    glVertex2f(229.5058594372752, 117.2083114063106)
    glVertex2f(231.0741715725304, 116.2313300761515)
    glVertex2f(232.7710338828065, 115.1257985709715)
    glVertex2f(232.7710338828065, 115.1257985709715)
    glVertex2f(234.3750408118579, 114.1810312564856)
    glVertex2f(236.258604062274, 113.1954458347562)
    glVertex2f(237.9669521266049, 112.4069774973726)
    glVertex2f(239.5876925978931, 111.5309015669465)
    glVertex2f(241.296040662224, 110.5015123486957)
    glVertex2f(242.807271642209, 109.8444554008761)
    glVertex2f(244.8441481804497, 109.0778889617532)
    glVertex2f(246.4463721176939, 108.3483047332004)
    glVertex2f(247.9916879725143, 107.6614976866134)
    glVertex2f(249.5713441796641, 106.9060099353678)
    glVertex2f(251.6347863764127, 106.1535432411102)
    glVertex2f(253.2801022312331, 105.4980554898646)
    glVertex2f(255.1688216093469, 104.8455887956071)
    glVertex2f(257.0232006351315, 104.1931221013495)
    glVertex2f(258.5685164899518, 103.5749957594213)
    glVertex2f(260.182513049431, 102.9912097698224)
    glVertex2f(262.1399131322035, 102.4074237802235)
    glVertex2f(264.1659939196347, 101.6175956766485)
    glVertex2f(268.4585379608025, 100.6217254590975)
    glVertex2f(270.6994855581892, 100.1653765039324)
    glVertex2f(272.6984004205137, 99.5796210041855)
    glVertex2f(276.13513123644, 98.5379726411015)
    glVertex2f(277.9587026897886, 98.1470110959691)
    glVertex2f(281.7461203236666, 97.5105687782706)
    glVertex2f(286.2349115934478, 96.974126460572)
    glVertex2f(288.4091698647481, 96.7286456880058)
    glVertex2f(294.9661651613397, 96.4965102595349)
    glVertex2f(302.5829997311739, 95.9071123463929)
    glVertex2f(310.1091576989863, 95.5897442393165)
    glVertex2f(319.0393964968513, 95.7313877924338)
    glVertex2f(325.7583484190043, 95.6830500088212)
    glVertex2f(332.1872736394817, 95.6347122252086)
    glVertex2f(335.5709184923646, 95.6347122252086)
    glVertex2f(340.5396977050059, 95.8978484726309) #V7 
    glEnd()

    #EKORR
    glColor3ub(186, 135, 89)
    glBegin(GL_POLYGON)
    glVertex2f(487.200718844477, 199.8802438499631) #P10
    glVertex2f(488.7320553380624, 202.6303991853819)
    glVertex2f(490, 205)
    glVertex2f(491.0319749875628, 207.0167776636904)
    glVertex2f(492.1847660887477, 208.9929909800075)
    glVertex2f(492.8435038608533, 211.2436783680352)
    glVertex2f(494.2707690337488, 214.262893156853)
    glVertex2f(495.2039808775651, 216.7880546165915)
    glVertex2f(497.8389319659876, 222.6617997512006)
    glVertex2f(500, 230)
    glVertex2f(500.6385674974366, 233.4211833622602)
    glVertex2f(501.3522000838843, 236.1110292650251)
    glVertex2f(502.3071368518009, 241.8010740998782)
    glVertex2f(502.8988595479272, 245.977940190182)
    glVertex2f(503.5253894614727, 249.7371196714554)
    glVertex2f(503.6298111137303, 253.4614919353095)
    glVertex2f(503.7342327659879, 257.046635329487)
    glVertex2f(503.8209303164183, 259.3474348902392)
    glVertex2f(503.7565948906987, 291.0236250287845)
    glVertex2f(503.4729225570964, 293.2447296579028)
    glVertex2f(503.0375080781438, 295.8572165316182)
    glVertex2f(502.7472317588422, 297.7440126070794)
    glVertex2f(502.4569554395405, 299.9210850018422)
    glVertex2f(502.021540960588, 302.2432955562559)
    glVertex2f(501.150712002683, 304.5655061106696)
    glVertex2f(500.6427284439051, 306.7425785054324)
    glVertex2f(500.4250212044288, 308.556805501068)
    glVertex2f(500, 310)
    glVertex2f(499.6267613263492, 311.3869996142597)
    glVertex2f(498.7559323684442, 312.9109502905937)
    glVertex2f(497.5948270912375, 313.9269174081497)
    glVertex2f(497.3772559898411, 312.9013170229082)
    glVertex2f(497.3072046954336, 311.9556245484077)
    glVertex2f(497.2721790482299, 311.1850603099258)
    glVertex2f(497.2721790482299, 310.2043421882214)
    glVertex2f(497.1546523865691, 308.9417963374849)
    glVertex2f(496.8810641113942, 307.2090705947095)
    glVertex2f(496.7074758362192, 306.0691194481467)
    glVertex2f(496.4882895151816, 304.9747663474465)
    glVertex2f(496.1983205799428, 302.597143925763)
    glVertex2f(495.2851325062065, 299.5941969356703)
    glVertex2f(494.9027403227565, 298.1350594680699)
    glVertex2f(494.4467598641314, 296.5847259087445)
    glVertex2f(493.6995833137813, 294.8608040742442)
    glVertex2f(493.1980048092938, 293.6840587900939)
    glVertex2f(492.6228380296313, 292.6897056893937)
    glVertex2f(492.0275493238891, 292.0536264089282)
    glVertex2f(491.3196715671662, 291.1605325517722) #N11
    glVertex2f(470.4676941694013, 261.4062015130951)
    glVertex2f(449.3217276603922, 290.89722672285) #P11
    glVertex2f(448.5556833734891, 291.5389412732622)
    glVertex2f(448, 292)
    glVertex2f(447.336261903495, 292.7922355618675)
    glVertex2f(446.8281696243307, 293.4696919340865)
    glVertex2f(446.3539501637775, 294.3503852179713)
    glVertex2f(445.4055112426709, 295.4004425949108)
    glVertex2f(444.4909451401753, 296.4843727904612)
    glVertex2f(443.9160355786823, 297.5346480268989)
    glVertex2f(443.5173741473379, 299.1655357005809)
    glVertex2f(443.2274385609056, 300.6514555810466)
    glVertex2f(442.9375029744733, 302.4997949445528)
    glVertex2f(442.647567388041, 304.348134308059)
    glVertex2f(442.3576318016087, 306.1964736715651)
    glVertex2f(442.4301156982168, 307.7186355003349)
    glVertex2f(442.2126640083925, 309.494490967233)
    glVertex2f(441.9589703702642, 311.2341044858271)
    glVertex2f(441.4085240334064, 312.9980547710079)
    glVertex2f(440.2100414320522, 310.8579072685894)
    glVertex2f(439.6108001313751, 308.7177597661708)
    glVertex2f(438.9259529306012, 305.3791296623979)
    glVertex2f(438.3267116299241, 302.8965585595925)
    glVertex2f(437.2138349286666, 299.3011107555293)
    glVertex2f(437.1282290285699, 296.7329337526271)
    glVertex2f(436.8714113282797, 294.2503626498216)
    glVertex2f(437, 291) #Q11
    glVertex2f(436.846179006764, 245.6149761266268)
    glVertex2f(436.5437047803231, 242.993532830806)
    glVertex2f(436.2412305538823, 239.8175534531769)
    glVertex2f(435.7875192142211, 236.9944606730622)
    glVertex2f(435.1825707613394, 234.0201307797271)
    glVertex2f(434.5776223084577, 231.1970379996124)
    glVertex2f(434.3323461532423, 229.9521413399795)
    glVertex2f(433.7280567642055, 227.5532955835001)
    glVertex2f(432.9772729778266, 225.1544498270208)
    glVertex2f(431.9701239960987, 222.3893680771868)
    glVertex2f(430.8897278156998, 219.4961037296774)
    glVertex2f(430.1755676286564, 217.9579125575838)
    glVertex2f(429.4430956419452, 216.2915387878157)
    glVertex2f(428.7106236552341, 214.6251650180477)
    glVertex2f(427.314003430061, 211.3685052225088)
    glVertex2f(426.7469754934215, 210.4148673290695)
    glVertex2f(426.7469754934215, 210.4148673290695)
    glVertex2f(425.4067276431826, 208.2498515709911)
    glVertex2f(424.8139257094231, 207.2188916861919)
    glVertex2f(423.4221298649443, 205.0281019309935)
    glVertex2f(421.7983680463856, 202.5537982074754)
    glVertex2f(420.200380224947, 200.5692004292368)
    glVertex2f(419.1436463430279, 199.4093705588377)
    glVertex2f(418, 198)
    glVertex2f(417.0301785791896, 196.9608408324395)
    glVertex2f(416, 196) #H17
    glVertex2f(415.0291750081199, 195.1277404849312)
    glVertex2f(414.0999593373728, 194.3653071140617)
    glVertex2f(413.0516134524274, 193.2693091434369)
    glVertex2f(411.9556154818026, 192.4353976440484)
    glVertex2f(410.7881393826589, 191.5061819733012)
    glVertex2f(409.5730111978357, 190.6007923453937)
    glVertex2f(408.0004923704177, 189.5286204176085)
    glVertex2f(406.8568423141135, 188.5994047468614)
    glVertex2f(405.3319755723747, 187.6940151189538)
    glVertex2f(403.9024130019946, 186.9792338337637)
    glVertex2f(402.3298941745765, 186.1691483772149)
    glVertex2f(400.4714628330823, 185.1684545779487) #T16
    glVertex2f(398.6606835772675, 184.2154128643619)#S16
    glVertex2f(436.7655002837649, 184.8867614553629)
    glVertex2f(434.891170160209, 142.905847749649)
    glVertex2f(436.7185536903968, 144.8211429386491)#L19
    glVertex2f(439.2776730469393, 148.4870600791274)
    glVertex2f(440.819688166531, 150.3899723543685)
    glVertex2f(442.2632767891276, 152.4241199589366)
    glVertex2f(443.8381007410511, 154.6879293898269)
    glVertex2f(445.2816893636477, 156.3205034913902)
    glVertex2f(446.6987631659317, 158.0265627726409)
    glVertex2f(448.4641460998264, 159.6420630719201)#T19
    glVertex2f(450.399867207399, 161.0200340298534)
    glVertex2f(452.1387353209813, 162.2667696584596)
    glVertex2f(453.8119857699, 163.4806964547341)
    glVertex2f(456.692566332849, 165.4383573503991)
    glVertex2f(459.0668039811769, 167.3886239900973)
    glVertex2f(461.2290561251897, 169.2540964280694)
    glVertex2f(463.4761024709287, 171.4587456729455)
    glVertex2f(465.5111633123526, 173.1546297074656)
    glVertex2f(467.8854009606804, 175.1048963471637)#E10
    glVertex2f(472.2523023495693, 179.938165845546)
    glVertex2f(474.3297602918562, 182.1428150904222)
    glVertex2f(477.5943370583071, 186.2129367732704)
    glVertex2f(479.5440363765504, 188.47334956101)
    glVertex2f(481.106624635311, 190.5672178277494)
    glVertex2f(482.6379611288963, 193.1923661024673)
    glVertex2f(485.7318858812421, 197.5676132269972)
    glEnd()

    #GARIS EKORR
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(448, 196)
    glVertex2f(416, 196) #H17
    glVertex2f(415.0291750081199, 195.1277404849312)
    glVertex2f(414.0999593373728, 194.3653071140617)
    glVertex2f(413.0516134524274, 193.2693091434369)
    glVertex2f(411.9556154818026, 192.4353976440484)
    glVertex2f(410.7881393826589, 191.5061819733012)
    glVertex2f(409.5730111978357, 190.6007923453937)
    glVertex2f(408.0004923704177, 189.5286204176085)
    glVertex2f(406.8568423141135, 188.5994047468614)
    glVertex2f(405.3319755723747, 187.6940151189538)
    glVertex2f(403.9024130019946, 186.9792338337637)
    glVertex2f(402.3298941745765, 186.1691483772149)
    glVertex2f(400.4714628330823, 185.1684545779487) #T16
    glVertex2f(436.7655002837649, 184.8867614553629)
    glVertex2f(436.7185536903968, 144.8211429386491)#L19
    glVertex2f(437.9401785356411, 144.5528218977708)
    glVertex2f(439.2776730469393, 146.1870600791274)
    glVertex2f(440.819688166531, 148.1899723543685)
    glVertex2f(442.2632767891276, 150.2241199589366)
    glVertex2f(443.8381007410511, 152.4879293898269)
    glVertex2f(445.2816893636477, 154.1205034913902)
    glVertex2f(446.6987631659317, 154.8265627726409)
    glVertex2f(448.4641460998264, 156.6420630719201)#T19
    glEnd()
    glColor3ub(75, 54, 33)
    glLineWidth(1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(218.9390350505558, 124.1500208574408)#L5 GARIS TENGAH KEPALA
    glVertex2f(221.3065932267011, 124.4208072416474)#O20
    glVertex2f(223.5436443775119, 124.6552758085959)
    glVertex2f(225.8875069300142, 124.965492911133)
    glVertex2f(227.955620946928, 125.3791157145158)
    glVertex2f(230, 126)
    glVertex2f(232.2641918154983, 126.8612640933042)
    glVertex2f(234.1311531014663, 127.6345803320513)
    glVertex2f(236.434115424502, 128.5886542796281)
    glVertex2f(238.2918927781418, 129.4360614935692)
    glVertex2f(239.8889294505691, 130.1508761223588)
    glVertex2f(241.4843408336784, 130.8354160204675)
    glVertex2f(243.4632642016192, 131.8794617122975)
    glVertex2f(245.8687944233344, 133.2299348192255)
    glVertex2f(248.3165269296411, 134.6648124953365)
    glVertex2f(250.4266411592159, 136.0996901714475)
    glVertex2f(252.7899690963396, 137.9565906934735)
    glVertex2f(255.4065107410123, 139.518075223359)
    glVertex2f(257.516624970587, 141.1639643224274)
    glVertex2f(259.7955483385277, 143.1896739828194)
    glVertex2f(262.0744717064684, 145.3841927815774)
    glVertex2f(264.1845859360432, 147.1144864498289)
    glVertex2f(265.872677319703, 149.0557915410379)
    glVertex2f(267.7717801263203, 151.3769171935704)
    glVertex2f(269.488679359232, 153.4828475752574)
    glVertex2f(271.4988609556652, 156.2796219702952)
    glVertex2f(273.916905484708, 159.5716584977876)
    glVertex2f(275.40949086785, 162.2764989286829)
    glVertex2f(277.3055851581261, 165.4072592684415)
    glVertex2f(278.5843464236611, 168.0088770155649)
    glVertex2f(279.7308220410374, 170.1695426021588)
    glVertex2f(280.9213928744665, 172.6829699171763)
    glVertex2f(281.891487627631, 174.8436355037702)
    glVertex2f(282.6852015165838, 176.8720154422054)
    glVertex2f(283.4348201894836, 179.1649666769581)
    glVertex2f(283.8757723500129, 181.413822695658)
    glVertex2f(284.339548138739, 183.3077938329918)
    glVertex2f(284.748713104447, 185.2172303396293)
    glVertex2f(285.4306547139603, 187.3994434900722)
    glVertex2f(285.66933427729, 189.377074157661)
    glVertex2f(285.8398196796683, 191.2865106642985)
    glVertex2f(285.976208001571, 193.6392092171197)
    glVertex2f(286.283081725852, 196.196490252795)
    glVertex2f(286.386433210016, 197.877090369461)
    glVertex2f(286.386433210016, 200.6501269143631)
    glVertex2f(286.1810230955789, 203.3204584020465)
    glVertex2f(286.1810230955789, 206.0934949469485)
    glVertex2f(285.8729079239232, 208.7638264346319)
    glVertex2f(285.5647927522674, 211.5368629795339)
    glVertex2f(285.0512674661745, 213.7450217097337)
    glVertex2f(284.6917997659095, 216.4667057260264)
    glVertex2f(283.7674542509423, 219.2910947995378)
    glVertex2f(283.2539289648494, 221.5506060583468)
    glVertex2f(282.6376986215379, 223.7587647885466)
    glVertex2f(282.5969830430009, 225.8133249342029)
    glVertex2f(282.3238292755912, 227.7689624354407)
    glVertex2f(281.9111137862676, 231.4244424837353)
    glVertex2f(280.9088047407676, 234.5787680092799)
    glVertex2f(279.6116989171793, 237.5267357901627)
    glVertex2f(278.314593093591, 240.887419060369)
    glVertex2f(277.6169005419681, 242.5777934413492)#I13 GARIS TENGAH KEPALA
    glEnd()

    #MATA IKAN
    glColor(1,0,0)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle) + center[0]
        y = radius * math.sin(angle) + center[1]
        glVertex2f(x, y)
    glEnd()


    # glColor(1,1,1)
    # glBegin(GL_LINES)
    # glVertex2f(193.3821416574563,218.9949817416802)
    # glVertex2f(436.7185536903968,218.9949817416802)
    # glVertex2f(436.7185536903968, 124.8211429386491)    
    # glVertex2f(193.3821416574563, 124.8211429386491)    
    # glEnd()
    glPopMatrix()
    
    return (50+xikan, 30+yikan)

    # return ('IKAN',193.3821416574563+xikan,436.7185536903968+xikan,144.8211429386491+yikan, 218.9949817416802+yikan)
#     self.ikan()
#     self.mata()

# def move_left():
#     global x
#     x -= 10
# def move_right():
#     global x
#     x += 10
# def move_up():
#     global y
#     y += 10
# def move_down():
#     global y
#     y -= 10
# def big ():
#     global b
#     b += 0.05
# def little ():
#     global b
#     b -= 0.05
# def putar():
#     global angel, z
#     angel += 5
#     z += 1
# def putarbalik():
#     global angel, z
#     angel -= 5
#     z -= 1

# keys = {
#     b'\x1b': sys.exit,  # Esc key
#     b'a': move_left,
#     b'd': move_right,
#     b'w': move_up,
#     b's': move_down,
#     b'x': big,
#     b'z': little,
#     b'q': putar,
#     b'e': putarbalik,
# }

# def keyboard(key, x, y):
#     if key in keys:
#         keys[key]()

# def iterate():
#     glViewport(0, 0, 1000, 1000)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     ikan(20)
#     glutSwapBuffers()


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(w, h)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("INI ADALAH IKAN BAKARR")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutKeyboardFunc(keyboard)
# glutMainLoop()