#!/usr/bin/env python3

SCALES = {
    "Minoric": 444,
    "Thaptic": 4341,
    "Lothic": 3414,
    "Phratic": 4143,
    "Aerathic": 1434,
    "Epathic": 4323,
    "Mynic": 3234,
    "Rothic": 2343,
    "Eporic": 3432,
    "Zyphic": 4431,
    "Epogic": 4314,
    "Lanic": 3144,
    "Pyrric": 1443,
    "Aeoloric": 4413,
    "Gonic": 4134,
    "Dalic": 1344,
    "Dygic": 3441,
    "Daric": 4332,
    "Lonic": 3324,
    "Phradic": 3243,
    "Bolic": 2433,
    "Saric": 4233,
    "Zoptic": 2334,
    "Aeraphic": 3342,
    "Byptic": 3423,
    "Aeolic": 4422,
    "Koptic": 4224,
    "Mixolyric": 2244,
    "Lydic": 2442,
    "Stathic": 4242,
    "Dadic": 2424,
    "Phrynic": 3333,
    "Epathitonic": 32322,
    "Mynitonic": 23223,
    "Rocritonic": 32232,
    "Pentatonic": 22323,
    "Thaptitonic": 23232,
    "Magitonic": 43221,
    "Daditonic": 32214,
    "Aeolyphritonic": 22143,
    "Gycritonic": 21432,
    "Pyritonic": 14322,
    "Gathitonic": 42321,
    "Ionitonic": 23214,
    "Phrynitonic": 32142,
    "Stathitonic": 21423,
    "Thalitonic": 14232,
    "Zolitonic": 42141,
    "Epogitonic": 21414,
    "Lanitonic": 14142,
    "Paptitonic": 41421,
    "Ionacritonic": 14214,
    "Phraditonic": 41412,
    "Aeoloritonic": 14124,
    "Gonitonic": 41241,
    "Dalitonic": 12414,
    "Dygitonic": 24141,
    "Aeracritonic": 41232,
    "Byptitonic": 12324,
    "Daritonic": 23241,
    "Lonitonic": 32412,
    "Ionycritonic": 24123,
    "Lothitonic": 41223,
    "Phratonic": 12234,
    "Aerathitonic": 22341,
    "Saritonic": 23412,
    "Zoptitonic": 34122,
    "Dolitonic": 44121,
    "Poritonic": 41214,
    "Aerylitonic": 12144,
    "Zagitonic": 21441,
    "Lagitonic": 14412,
    "Molitonic": 43311,
    "Staptitonic": 33114,
    "Mothitonic": 31143,
    "Aeritonic": 11433,
    "Ragitonic": 14331,
    "Ionaditonic": 43212,
    "Bocritonic": 32124,
    "Gythitonic": 21243,
    "Pagitonic": 12432,
    "Aeolythitonic": 24321,
    "Zacritonic": 43131,
    "Laritonic": 31314,
    "Thacritonic": 13143,
    "Styditonic": 31431,
    "Loritonic": 14313,
    "Aeolyritonic": 43113,
    "Goritonic": 31134,
    "Aeoloditonic": 11343,
    "Doptitonic": 13431,
    "Aeraphitonic": 34311,
    "Zathitonic": 42411,
    "Raditonic": 24114,
    "Stonitonic": 41142,
    "Syptitonic": 11424,
    "Ionythitonic": 14241,
    "Aeolanitonic": 42231,
    "Danitonic": 22314,
    "Ionaritonic": 23142,
    "Dynitonic": 31422,
    "Zyditonic": 14223,
    "Aeolacritonic": 42123,
    "Zythitonic": 21234,
    "Dyritonic": 12342,
    "Koptitonic": 23421,
    "Thocritonic": 34212,
    "Lycritonic": 41331,
    "Daptitonic": 13314,
    "Kygitonic": 33141,
    "Mocritonic": 31413,
    "Zynitonic": 14133,
    "Epygitonic": 41322,
    "Zaptitonic": 13224,
    "Kagitonic": 32241,
    "Zogitonic": 22413,
    "Epyritonic": 24132,
    "Zothitonic": 41313,
    "Phrolitonic": 13134,
    "Ionagitonic": 31341,
    "Aeolapritonic": 13413,
    "Kyritonic": 34131,
    "Ionyptitonic": 41133,
    "Gyritonic": 11334,
    "Zalitonic": 13341,
    "Stolitonic": 33411,
    "Bylitonic": 34113,
    "Thoditonic": 33231,
    "Dogitonic": 32313,
    "Phralitonic": 23133,
    "Garitonic": 31332,
    "Soptitonic": 13323,
    "Kataritonic": 33222,
    "Sylitonic": 32223,
    "Thonitonic": 22233,
    "Phropitonic": 22332,
    "Staditonic": 23322,
    "Lyditonic": 33132,
    "Mythitonic": 31323,
    "Sogitonic": 13233,
    "Gothitonic": 32331,
    "Rothitonic": 23313,
    "Zylitonic": 44211,
    "Zoditonic": 42114,
    "Zaritonic": 21144,
    "Phrythitonic": 11442,
    "Rolitonic": 14421,
    "Ranitonic": 44112,
    "Laditonic": 41124,
    "Poditonic": 11244,
    "Ionothitonic": 12441,
    "Kanitonic": 24411,
    "Ryphitonic": 43122,
    "Gylitonic": 31224,
    "Aeolycritonic": 12243,
    "Pynitonic": 22431,
    "Zanitonic": 24312,
    "Phronitonic": 42312,
    "Banitonic": 23124,
    "Aeronitonic": 31242,
    "Golitonic": 12423,
    "Dyptitonic": 24231,
    "Aerynitonic": 42213,
    "Palitonic": 22134,
    "Stothitonic": 21342,
    "Aerophitonic": 13422,
    "Katagitonic": 34221,
    "Ionoditonic": 42132,
    "Bogitonic": 21324,
    "Mogitonic": 13242,
    "Docritonic": 32421,
    "Epaditonic": 24213,
    "Mixitonic": 33321,
    "Phrothitonic": 33213,
    "Katycritonic": 32133,
    "Ionalitonic": 21333,
    "Loptitonic": 13332,
    "Thyritonic": 33312,
    "Thoptitonic": 33123,
    "Bycritonic": 31233,
    "Pathitonic": 12333,
    "Myditonic": 23331,
    "Bolitonic": 42222,
    "Bothitonic": 22224,
    "Kataditonic": 22242,
    "Koditonic": 22422,
    "Tholitonic": 24222,
    "Epathimic": 322122,
    "Mynimic": 221223,
    "Rocrimic": 212232,
    "Eporimic": 122322,
    "Thaptimic": 223221,
    "Lothimic": 232212,
    "Dyrimic": 421221,
    "Koptimic": 212214,
    "Thocrimic": 122142,
    "Aeolanimic": 221421,
    "Danimic": 214212,
    "Ionarimic": 142122,
    "Daptimic": 414111,
    "Kygimic": 141114,
    "Mocrimic": 411141,
    "Zynimic": 111414,
    "Aeolimic": 114141,
    "Zythimic": 141411,
    "Epygimic": 412311,
    "Zaptimic": 123114,
    "Kagimic": 231141,
    "Zogimic": 311412,
    "Epyrimic": 114123,
    "Lycrimic": 141231,
    "Bylimic": 412221,
    "Zothimic": 122214,
    "Phrolimic": 222141,
    "Ionagimic": 221412,
    "Aeolaphimic": 214122,
    "Kycrimic": 141222,
    "Garimic": 412212,
    "Soptimic": 122124,
    "Ionyptimic": 221241,
    "Gyrimic": 212412,
    "Zalimic": 124122,
    "Stolimic": 241221,
    "Thonimic": 411411,
    "Stadimic": 114114,
    "Thodimic": 141141,
    "Mythimic": 411321,
    "Sogimic": 113214,
    "Gogimic": 132141,
    "Rothimic": 321411,
    "Katarimic": 214113,
    "Sylimic": 141132,
    "Mixolimic": 323211,
    "Dadimic": 232113,
    "Aeolyphimic": 321132,
    "Gycrimic": 211323,
    "Pyrimic": 113232,
    "Lydimic": 132321,
    "Ionacrimic": 323112,
    "Gathimic": 231123,
    "Ionynimic": 311232,
    "Phrynimic": 112323,
    "Stathimic": 123231,
    "Thatimic": 232311,
    "Dalimic": 322311,
    "Dygimic": 223113,
    "Zolimic": 231132,
    "Epogimic": 311322,
    "Lanimic": 113223,
    "Paptimic": 132231,
    "Darmic": 322212,
    "Lonimic": 222123,
    "Ionycrimic": 221232,
    "Phradimic": 212322,
    "Aeolorimic": 123222,
    "Gonimic": 232221,
    "Phracrimic": 321222,
    "Aerathimic": 212223,
    "Sarimic": 122232,
    "Zoptimic": 222321,
    "Zeracrimic": 223212,
    "Byptimic": 232122,
    "Starimic": 432111,
    "Phrathimic": 321114,
    "Saptimic": 211143,
    "Aerodimic": 111432,
    "Macrimic": 114321,
    "Rogimic": 143211,
    "Bygimic": 431121,
    "Thycrimic": 311214,
    "Aeoladimic": 112143,
    "Dylimic": 121431,
    "Eponimic": 214311,
    "Katygimic": 143112,
    "Stalimic": 423111,
    "Stoptimic": 231114,
    "Zygimic": 311142,
    "Kataptimic": 111423,
    "Aeolaptimic": 114231,
    "Pothimic": 142311,
    "Rycrimic": 422121,
    "Ronimic": 221214,
    "Stycrimic": 212142,
    "Katorimic": 121422,
    "Epythimic": 214221,
    "Kaptimic": 142212,
    "Katythimic": 421311,
    "Madimic": 213114,
    "Aerygimic": 131142,
    "Pylimic": 311421,
    "Ionathimic": 114213,
    "Morimic": 142131,
    "Aerycrimic": 421131,
    "Ganimic": 211314,
    "Eparimic": 113142,
    "Lyrimic": 131421,
    "Phraptimic": 314211,
    "Bacrimic": 142113,
    "Phralimic": 413211,
    "Phrogimic": 132114,
    "Rathimic": 321141,
    "Katocrimic": 211413,
    "Phryptimic": 114132,
    "Katynimic": 141321,
    "Solimic": 413121,
    "Ionolimic": 131214,
    "Ionophimic": 312141,
    "Aeologimic": 121413,
    "Zadimic": 214131,
    "Sygimic": 141312,
    "Thogimic": 413112,
    "Rythimic": 131124,
    "Donimic": 311241,
    "Aeoloptimic": 112413,
    "Panimic": 124131,
    "Lodimic": 241311,
    "Laptimic": 412131,
    "Lygimic": 121314,
    "Logimic": 213141,
    "Lalimic": 131412,
    "Sothimic": 314121,
    "Phrocrimic": 141213,
    "Modimic": 412122,
    "Barimic": 121224,
    "Poptimic": 212241,
    "Sagimic": 122412,
    "Aelothimic": 224121,
    "Socrimic": 241212,
    "Syrimic": 412113,
    "Stodimic": 121134,
    "Ionocrimic": 211341,
    "Zycrimic": 113412,
    "Ionygimic": 134121,
    "Katathimic": 341211,
    "Bolimic": 411312,
    "Bothimic": 113124,
    "Katadimic": 131241,
    "Kodimic": 312411,
    "Tholimic": 124113,
    "Ralimic": 241131,
    "Kanimic": 411231,
    "Zylimic": 112314,
    "Zodimic": 123141,
    "Zarimic": 231411,
    "Phrythimic": 314112,
    "Rorimic": 141123,
    "Pynimic": 411132,
    "Zanimic": 111324,
    "Ranimic": 113241,
    "Ladimic": 132411,
    "Podimic": 324111,
    "Ionothimic": 241113,
    "Kytrimic": 411123,
    "Golimic": 111234,
    "Dyptimic": 112341,
    "Ryrimic": 123411,
    "Gylimic": 234111,
    "Aeolycrimic": 341112,
    "Palimic": 332211,
    "Stothimic": 322113,
    "Aeronimic": 221133,
    "Katagimic": 211332,
    "Phronimic": 113322,
    "Banimic": 133221,
    "Ionodimic": 331311,
    "Bogimic": 313113,
    "Mogimic": 131133,
    "Docrimic": 311331,
    "Epadimic": 113313,
    "Aerynimic": 133131,
    "Mydimic": 331131,
    "Thyptimic": 311313,
    "Phrothimic": 113133,
    "Katycrimic": 131331,
    "Ionalimic": 313311,
    "Loptimic": 133113,
    "Zagimic": 331122,
    "Lagimic": 311223,
    "Thyrimic": 112233,
    "Thothimic": 122331,
    "Bycrimic": 223311,
    "Pathimic": 233112,
    "Mothimic": 322131,
    "Aeranimic": 221313,
    "Ragimic": 213132,
    "Dolimic": 131322,
    "Porimic": 313221,
    "Aerylimic": 132213,
    "Bocrimic": 321312,
    "Gythimic": 213123,
    "Pagimic": 131232,
    "Aeolythimic": 312321,
    "Molimic": 123213,
    "Staptimic": 232131,
    "Zacrimic": 321231,
    "Larimic": 212313,
    "Thacrimic": 123132,
    "Stydimic": 231321,
    "Lorimic": 313212,
    "Ionadimic": 132123,
    "Ionythimic": 313131,
    "Aerythimic": 131313,
    "Dynimic": 313122,
    "Zydimic": 131223,
    "Zathimic": 312231,
    "Radimic": 122313,
    "Stonimic": 223131,
    "Syptimic": 231312,
    "Ponimic": 441111,
    "Kadimic": 411114,
    "Gynimic": 111144,
    "Thydimic": 111441,
    "Polimic": 114411,
    "Thanimic": 144111,
    "Lathimic": 431211,
    "Aeralimic": 312114,
    "Kynimic": 121143,
    "Stynimic": 211431,
    "Epytimic": 114312,
    "Katoptimic": 143121,
    "Galimic": 431112,
    "Kathimic": 311124,
    "Lylimic": 111243,
    "Epalimic": 112431,
    "Epacrimic": 124311,
    "Sathimic": 243111,
    "Katanimic": 422211,
    "Katyrimic": 222114,
    "Rynimic": 221142,
    "Pogimic": 211422,
    "Aeraptimic": 114222,
    "Epylimic": 142221,
    "Manimic": 421212,
    "Marimic": 212124,
    "Locrimic": 121242,
    "Rylimic": 212421,
    "Epatimic": 124212,
    "Byrimic": 242121,
    "Kocrimic": 421113,
    "Korimic": 211134,
    "Lynimic": 111342,
    "Malimic": 113421,
    "Synimic": 134211,
    "Phragimic": 342111,
    "Mycrimic": 411222,
    "Ionorimic": 112224,
    "Phrydimic": 122241,
    "Zyptimic": 222411,
    "Katothimic": 224112,
    "Phrylimic": 241122,
    "Aerothimic": 411213,
    "Stagimic": 112134,
    "Dorimic": 121341,
    "Phrycrimic": 213411,
    "Kyptimic": 134112,
    "Ionylimic": 341121,
    "Epynimic": 333111,
    "Ionogimic": 331113,
    "Kydimic": 311133,
    "Gaptimic": 111333,
    "Tharimic": 113331,
    "Ionaphimic": 133311,
    "Thoptimic": 332121,
    "Bagimic": 321213,
    "Kyrimic": 212133,
    "Sonimic": 121332,
    "Aeolonimic": 213321,
    "Rygimic": 133212,
    "Thagimic": 332112,
    "Kolimic": 321123,
    "Dycrimic": 211233,
    "Epycrimic": 112332,
    "Gocrimic": 123321,
    "Katolimic": 233211,
    "Dagimic": 331221,
    "Aeolydimic": 312213,
    "Parimic": 122133,
    "Ionaptimic": 221331,
    "Thylimic": 213312,
    "Lolimic": 133122,
    "Thalimic": 331212,
    "Stygimic": 312123,
    "Aeolygimic": 121233,
    "Aerogimic": 212331,
    "Dacrimic": 123312,
    "Baptimic": 233121,
    "Stythimic": 323121,
    "Kothimic": 231213,
    "Pygimic": 312132,
    "Rodimic": 121323,
    "Sorimic": 213231,
    "Monimic": 132312,
    "Aeragimic": 322221,
    "Epothimic": 222213,
    "Salimic": 222132,
    "Lyptimic": 221322,
    "Katonimic": 213222,
    "Gygimic": 132222,
    "Aeradimic": 321321,
    "Zyrimic": 213213,
    "Stylimic": 132132,
    "Lythimic": 312312,
    "Dodimic": 123123,
    "Katalimic": 231231,
    "Boptimic": 312222,
    "Stogimic": 122223,
    "Thynimic": 222231,
    "Aeolathimic": 222312,
    "Bythimic": 223122,
    "Padimic": 231222,
    "Dathimic": 422112,
    "Epagimic": 221124,
    "Raptimic": 211242,
    "Epolimic": 112422,
    "Sythimic": 124221,
    "Sydimic": 242211,
    "Gacrimic": 421122,
    "Borimic": 211224,
    "Sycrimic": 112242,
    "Gadimic": 122421,
    "Aeolocrimic": 224211,
    "Phrygimic": 242112,
    "WholeTone": 222222,
    "Lydian": 2221221,
    "Mixolydian": 2212212,
    "Aeolian": 2122122,
    "Locrian": 1221222,
    "Ionian": 2212221,
    "Dorian": 2122212,
    "Phrygian": 1222122,
    "Ionythian": 4122111,
    "Aeolyrian": 1221114,
    "Gorian": 2211141,
    "Aeolodian": 2111412,
    "Doptian": 1114122,
    "Aeraphian": 1141221,
    "Zacrian": 1412211,
    "Ionarian": 4113111,
    "Dynian": 1131114,
    "Zydian": 1311141,
    "Zathian": 3111411,
    "Radian": 1114113,
    "Stonian": 1141131,
    "Syptian": 1411311,
    "Aeolacrian": 4111311,
    "Zythian": 1113114,
    "Dyrian": 1131141,
    "Koptian": 1311411,
    "Thocrian": 3114111,
    "Aeolanian": 1141113,
    "Danian": 1411131,
    "Zogian": 4111221,
    "Epyrian": 1112214,
    "Lycrian": 1122141,
    "Daptian": 1221411,
    "Kygian": 2214111,
    "Mocrian": 2141112,
    "Zynian": 1411122,
    "Phrolian": 3221211,
    "Ionagian": 2212113,
    "Aeodian": 2121132,
    "Kycrian": 1211322,
    "Epygian": 2113221,
    "Zaptian": 1132212,
    "Kagian": 1322121,
    "Soptian": 3221112,
    "Ionyptian": 2211123,
    "Gyrian": 2111232,
    "Zalian": 1112322,
    "Stolian": 1123221,
    "Bylian": 1232211,
    "Zothian": 2322111,
    "Thonian": 3212211,
    "Phrorian": 2122113,
    "Stadian": 1221132,
    "Thodian": 2211321,
    "Dogian": 2113212,
    "Mixopyrian": 1132122,
    "Garian": 1321221,
    "Epathian": 3211311,
    "Mythian": 2113113,
    "Sogian": 1131132,
    "Gogian": 1311321,
    "Rothian": 3113211,
    "Katarian": 1132113,
    "Stylian": 1321131,
    "Stathian": 3211122,
    "Mixonyphian": 2111223,
    "Magian": 1112232,
    "Dadian": 1122321,
    "Aeolylian": 1223211,
    "Gycrian": 2232111,
    "Pyrian": 2321112,
    "Epogian": 3113112,
    "Lanian": 1131123,
    "Paptian": 1311231,
    "Ionacrian": 3112311,
    "Gathian": 1123113,
    "Ionyphian": 1231131,
    "Phrynian": 2311311,
    "Ionycrian": 3112212,
    "Phradian": 1122123,
    "Aeolorian": 1221231,
    "Gonian": 2212311,
    "Dalian": 2123112,
    "Dygian": 1231122,
    "Zolian": 2311221,
    "Aerathian": 3112122,
    "Sarian": 1121223,
    "Zoptian": 1212231,
    "Aeracrian": 2122311,
    "Byptian": 1223112,
    "Darian": 2231121,
    "Lonian": 2311212,
    "Aeopian": 4212111,
    "Rygian": 2121114,
    "Epynian": 1211142,
    "Ionogian": 2111421,
    "Kydian": 1114212,
    "Gaptian": 1142121,
    "Tharian": 1421211,
    "Epycrian": 4211121,
    "Gocrian": 2111214,
    "Katolian": 1112142,
    "Thoptian": 1121421,
    "Bagian": 1214211,
    "Kyrian": 2142111,
    "Sonian": 1421112,
    "Parian": 4131111,
    "Ionaptian": 1311114,
    "Thylian": 3111141,
    "Lolian": 1111413,
    "Thagian": 1114131,
    "Kolian": 1141311,
    "Dycrian": 1413111,
    "Stygian": 4121211,
    "Aeolygian": 1212114,
    "Aerogian": 2121141,
    "Dacrian": 1211412,
    "Baptian": 2114121,
    "Dagian": 1141212,
    "Aeolydian": 1412121,
    "Stythian": 4121121,
    "Kothian": 1211214,
    "Pygian": 2112141,
    "Rodian": 1121412,
    "Sorian": 1214121,
    "Monian": 2141211,
    "Thalian": 1412112,
    "Zorian": 4121112,
    "Aeragian": 1211124,
    "Epothian": 2111241,
    "Salian": 1112412,
    "Lyptian": 1124121,
    "Katonian": 1241211,
    "Gyphian": 2412111,
    "Thacrian": 4112211,
    "Dodian": 1122114,
    "Aeolyptian": 1221141,
    "Aeolonian": 2211411,
    "Aeradian": 2114112,
    "Aeolagian": 1141122,
    "Zyrian": 1411221,
    "Aeolathian": 4112121,
    "Bythian": 1121214,
    "Padian": 1212141,
    "Rolian": 2121411,
    "Pydian": 1214112,
    "Thygian": 2141121,
    "Katalian": 1411212,
    "Saptian": 4111212,
    "Aerodian": 1112124,
    "Macrian": 1121241,
    "Rogian": 1212411,
    "Boptian": 2124111,
    "Stogian": 1241112,
    "Thynian": 2411121,
    "Thycrian": 4111131,
    "Aeoladian": 1111314,
    "Dylian": 1113141,
    "Eponian": 1131411,
    "Katygian": 1314111,
    "Starian": 3141111,
    "Phrathian": 1411113,
    "Stalian": 3311211,
    "Stoptian": 3112113,
    "Zygian": 1121133,
    "Kataptian": 1211331,
    "Aeolaptian": 2113311,
    "Pothian": 1133112,
    "Bygian": 1331121,
    "Morian": 3231111,
    "Rycrian": 2311113,
    "Ronian": 3111132,
    "Stycrian": 1111323,
    "Katorian": 1113231,
    "Epythian": 1132311,
    "Kaptian": 1323111,
    "Phraptian": 3222111,
    "Bacrian": 2221113,
    "Katythian": 2211132,
    "Madian": 2111322,
    "Aerygian": 1113222,
    "Pylian": 1132221,
    "Ionathian": 1322211,
    "Katocrian": 3213111,
    "Phryptian": 2131113,
    "Katynian": 1311132,
    "Aerycrian": 3111321,
    "Ganian": 1113213,
    "Eparian": 1132131,
    "Lyrian": 1321311,
    "Ionopian": 3212112,
    "Aeologian": 2121123,
    "Zadian": 1211232,
    "Sygian": 2112321,
    "Phralian": 1123212,
    "Phrogian": 1232121,
    "Rathian": 2321211,
    "Rythian": 3211212,
    "Donian": 2112123,
    "Aeoloptian": 1121232,
    "Panian": 1212321,
    "Lodian": 2123211,
    "Solian": 1232112,
    "Ionolian": 2321121,
    "Laptian": 3211131,
    "Lygian": 2111313,
    "Logian": 1113132,
    "Lalian": 1131321,
    "Sothian": 1313211,
    "Phrocrian": 3132111,
    "Thogian": 1321113,
    "Katathian": 3131211,
    "Modian": 1312113,
    "Barian": 3121131,
    "Mixolocrian": 1211313,
    "Sagian": 2113131,
    "Aeolothian": 1131312,
    "Socrian": 1313121,
    "Tholian": 3131121,
    "Ralian": 1311213,
    "Syrian": 3112131,
    "Stodian": 1121313,
    "Ionocrian": 1213131,
    "Zycrian": 2131311,
    "Ionygian": 1313112,
    "Zarian": 3131112,
    "Phrythian": 1311123,
    "Rorian": 3111231,
    "Bolian": 1112313,
    "Bothian": 1123131,
    "Katadian": 1231311,
    "Kodian": 2313111,
    "Ranian": 3123111,
    "Ladian": 1231113,
    "Podian": 2311131,
    "Ionothian": 3111312,
    "Kanian": 1113123,
    "Zylian": 1131231,
    "Zodian": 1312311,
    "Golian": 3122211,
    "Dyptian": 1222113,
    "Ryphian": 2221131,
    "Gylian": 2211312,
    "Aeolycrian": 2113122,
    "Pynian": 1131222,
    "Zanian": 1312221,
    "Palian": 3122121,
    "Stothian": 1221213,
    "Aerorian": 2212131,
    "Katagian": 2121312,
    "Phronian": 1213122,
    "Banian": 2131221,
    "Aeronian": 1312212,
    "Loptian": 3121311,
    "Ionodian": 1213113,
    "Bogian": 2131131,
    "Mogian": 1311312,
    "Docrian": 3113121,
    "Epadian": 1131213,
    "Aerynian": 1312131,
    "Bycrian": 3121221,
    "Pathian": 1212213,
    "Mydian": 2122131,
    "Thyptian": 1221312,
    "Phrothian": 2213121,
    "Katycrian": 2131212,
    "Ionalian": 1312122,
    "Dolian": 3112221,
    "Porian": 1122213,
    "Aerylian": 1222131,
    "Zagian": 2221311,
    "Lagian": 2213112,
    "Tyrian": 2131122,
    "Mixonorian": 1311222,
    "Pagian": 3111222,
    "Aeolythian": 1112223,
    "Molian": 1122231,
    "Staptian": 1222311,
    "Mothian": 2223111,
    "Aeranian": 2231112,
    "Ragian": 2311122,
    "Larian": 2222121,
    "Lythian": 2221212,
    "Stydian": 2212122,
    "Lorian": 2121222,
    "Ionadian": 1212222,
    "Bocrian": 2122221,
    "Mixolythian": 1222212,
    "Thadian": 4311111,
    "Sanian": 3111114,
    "Ionydian": 1111143,
    "Epydian": 1111431,
    "Katydian": 1114311,
    "Mathian": 1143111,
    "Aeryptian": 1431111,
    "Pythian": 4221111,
    "Katylian": 2211114,
    "Bydian": 2111142,
    "Bynian": 1111422,
    "Galian": 1114221,
    "Zonian": 1142211,
    "Myrian": 1422111,
    "Katogian": 4211211,
    "Stacrian": 2112114,
    "Styrian": 1121142,
    "Ionyrian": 1211421,
    "Phrodian": 2114211,
    "Pycrian": 1142112,
    "Gyptian": 1421121,
    "Katacrian": 4112112,
    "Sodian": 1121124,
    "Bathian": 1211241,
    "Mylian": 2112411,
    "Godian": 1124112,
    "Thorian": 1241121,
    "Zocrian": 2411211,
    "Stanian": 4111122,
    "Epanian": 1111224,
    "Konian": 1112241,
    "Stocrian": 1122411,
    "Kalian": 1224111,
    "Phroptian": 2241111,
    "Dydian": 2411112,
    "Katyptian": 4111113,
    "Epodian": 1111134,
    "Mygian": 1111341,
    "Pacrian": 1113411,
    "Aerocrian": 1134111,
    "Aeolarian": 1341111,
    "Kythian": 3411111,
    "Bonian": 3321111,
    "Badian": 3211113,
    "Katodian": 2111133,
    "Sadian": 1111332,
    "Dothian": 1113321,
    "Moptian": 1133211,
    "Aeryrian": 1332111,
    "Epagian": 3312111,
    "Raptian": 3121113,
    "Epolian": 1211133,
    "Sythian": 2111331,
    "Sydian": 1113312,
    "Epocrian": 1133121,
    "Kylian": 1331211,
    "Gacrian": 3311121,
    "Borian": 3111213,
    "Sycrian": 1112133,
    "Gadian": 1121331,
    "Aeolocrian": 1213311,
    "Mixodorian": 2133111,
    "Dathian": 1331112,
    "Katoptian": 3311112,
    "Ponian": 3111123,
    "Kadian": 1111233,
    "Gynian": 1112331,
    "Thyphian": 1123311,
    "Polian": 1233111,
    "Thanian": 2331111,
    "Epacrian": 3221121,
    "Sathian": 2211213,
    "Lathian": 2112132,
    "Aeralian": 1121322,
    "Kynian": 1213221,
    "Stynian": 2132211,
    "Epyphian": 1322112,
    "Pogian": 3212121,
    "Aeraptian": 2121213,
    "Epylian": 1212132,
    "Gamian": 2121321,
    "Kathian": 1213212,
    "Lylian": 2132121,
    "Epalian": 1321212,
    "Eporian": 3211221,
    "Rylian": 2112213,
    "Epaptian": 1122132,
    "Byrian": 1221321,
    "Katanian": 2213211,
    "Katyrian": 2132112,
    "Rynian": 1321122,
    "Korian": 3122112,
    "Lynian": 1221123,
    "Malian": 2211231,
    "Synian": 2112312,
    "Phragian": 1123122,
    "Manian": 1231221,
    "Marian": 2312211,
    "Mycrian": 3121212,
    "Ionorian": 1212123,
    "Phrydian": 2121231,
    "Zyptian": 1212312,
    "Katothian": 2123121,
    "Phrylian": 1231212,
    "Kocrian": 2312121,
    "Ionanian": 3121122,
    "Aerothian": 1211223,
    "Stagian": 2112231,
    "Lothian": 1122312,
    "Phrycrian": 1223121,
    "Kyptian": 2231211,
    "Ionylian": 2312112,
    "Gydian": 4211112,
    "Kogian": 2111124,
    "Rarian": 1111242,
    "Aerolian": 1112421,
    "Karian": 1124211,
    "Myptian": 1242111,
    "Rydian": 2421111,
    "Aeolynian": 2222211,
    "Aeroptian": 2222112,
    "Phryrian": 2221122,
    "Gothian": 2211222,
    "Storian": 2112222,
    "Pyptian": 1122222,
    "Thydian": 1222221,
    "Aerycryllic": 22122111,
    "Gadyllic": 21221112,
    "Solyllic": 12211122,
    "Zylyllic": 22111221,
    "Mixodyllic": 21112212,
    "Soryllic": 11122122,
    "Godyllic": 11221221,
    "Epiphyllic": 12212211,
    "Pynyllic": 41112111,
    "Bocryllic": 11121114,
    "Kogyllic": 11211141,
    "Raryllic": 12111411,
    "Zycryllic": 21114111,
    "Mycryllic": 11141112,
    "Laptyllic": 11411121,
    "Pylyllic": 14111211,
    "Pothyllic": 32111211,
    "Phronyllic": 21112113,
    "Stynyllic": 11121132,
    "Rathyllic": 11211321,
    "Aeryptyllic": 12113211,
    "Zydyllic": 21132111,
    "Katolyllic": 11321112,
    "Rythyllic": 13211121,
    "Locryllic": 31131111,
    "Bylyllic": 11311113,
    "Sogyllic": 13111131,
    "Ionycryllic": 31111311,
    "Koptyllic": 11113113,
    "Epyryllic": 11131131,
    "Soptyllic": 11311311,
    "Aeolylyllic": 13113111,
    "Aeracryllic": 31122111,
    "Epygyllic": 11221113,
    "Thonyllic": 12211131,
    "Lanyllic": 22111311,
    "Phrynyllic": 21113112,
    "Lycryllic": 11131122,
    "Ionyptyllic": 11311221,
    "Epathyllic": 13112211,
    "Dydyllic": 31121211,
    "Thogyllic": 11212113,
    "Rygyllic": 12121131,
    "Bycryllic": 21211311,
    "Zacryllic": 12113112,
    "Panyllic": 21131121,
    "Dyryllic": 11311212,
    "Zathyllic": 13112121,
    "Dagyllic": 31121112,
    "Katalyllic": 11211123,
    "Katoryllic": 12111231,
    "Dodyllic": 21112311,
    "Zogyllic": 11123112,
    "Madyllic": 11231121,
    "Dycryllic": 12311211,
    "Aeologyllic": 23112111,
    "Sydyllic": 31113111,
    "Katogyllic": 11131113,
    "Zygyllic": 11311131,
    "Aeralyllic": 13111311,
    "Bacryllic": 31112211,
    "Aerygyllic": 11122113,
    "Dathyllic": 11221131,
    "Boptyllic": 12211311,
    "Bagyllic": 22113111,
    "Mathyllic": 21131112,
    "Styptyllic": 11311122,
    "Zolyllic": 13111221,
    "Rocryllic": 22212111,
    "Zyryllic": 22121112,
    "Sagyllic": 21211122,
    "Epinyllic": 12111222,
    "Katagyllic": 21112221,
    "Ragyllic": 11122212,
    "Gothyllic": 11222121,
    "Lythyllic": 12221211,
    "Ionocryllic": 22211121,
    "Gocryllic": 22111212,
    "Epiryllic": 21112122,
    "Aeradyllic": 11121222,
    "Staptyllic": 11212221,
    "Danyllic": 12122211,
    "Goptyllic": 21222111,
    "Epocryllic": 12221112,
    "Ionoptyllic": 22121121,
    "Aeoloryllic": 21211212,
    "Thydyllic": 12112122,
    "Gycryllic": 21121221,
    "Lyryllic": 11212212,
    "Mogyllic": 12122121,
    "Katodyllic": 21221211,
    "Moptyllic": 12212112,
    "Dolyllic": 41211111,
    "Moryllic": 12111114,
    "Bydyllic": 21111141,
    "Pocryllic": 11111412,
    "Phracryllic": 11114121,
    "Gyryllic": 11141211,
    "Phrygyllic": 11412111,
    "Dogyllic": 14121111,
    "Thagyllic": 41121111,
    "Thoptyllic": 11211114,
    "Phraptyllic": 12111141,
    "Gylyllic": 21111411,
    "Phralyllic": 11114112,
    "Dygyllic": 11141121,
    "Ronyllic": 11411211,
    "Epogyllic": 14112111,
    "Aeoladyllic": 41111211,
    "Kocryllic": 11112114,
    "Lodyllic": 11121141,
    "Bynyllic": 11211411,
    "Kydyllic": 12114111,
    "Bygyllic": 21141111,
    "Phryptyllic": 11411112,
    "Ionayllic": 14111121,
    "Phroryllic": 41111121,
    "Thyphyllic": 11111214,
    "Poptyllic": 11112141,
    "Mixonyllic": 11121411,
    "Paptyllic": 11214111,
    "Storyllic": 12141111,
    "Phrycryllic": 21411111,
    "Palyllic": 14111112,
    "Phranyllic": 32211111,
    "Stydyllic": 22111113,
    "Zadyllic": 21111132,
    "Zalyllic": 11111322,
    "Zocryllic": 11113221,
    "Katocryllic": 11132211,
    "Aerathyllic": 11322111,
    "Stoptyllic": 13221111,
    "Lydyllic": 32121111,
    "Radyllic": 21211113,
    "Stagyllic": 12111132,
    "Ionoryllic": 21111321,
    "Phrodyllic": 11113212,
    "Aeragyllic": 11132121,
    "Banyllic": 11321211,
    "Epothyllic": 13212111,
    "Zoryllic": 32112111,
    "Phrolyllic": 21121113,
    "Kolyllic": 11211132,
    "Thodyllic": 12111321,
    "Socryllic": 21113211,
    "Aeolyllic": 11132112,
    "Zythyllic": 11321121,
    "Aeoryllic": 13211211,
    "Mixolydyllic": 32111112,
    "Mixonyphyllic": 21111123,
    "Aeolanyllic": 11111232,
    "Thocryllic": 11112321,
    "Kygyllic": 11123211,
    "Ionagyllic": 11232111,
    "Gogyllic": 12321111,
    "Phradyllic": 23211111,
    "Ioniptyllic": 31311111,
    "Kycryllic": 13111113,
    "Aeolaptyllic": 31111131,
    "Rodyllic": 11111313,
    "Ionathyllic": 11113131,
    "Pythyllic": 11131311,
    "Zonyllic": 11313111,
    "Ryryllic": 13131111,
    "Aeolothyllic": 31221111,
    "Ionyryllic": 12211113,
    "Rydyllic": 22111131,
    "Gonyllic": 21111312,
    "Rolyllic": 11113122,
    "Katydyllic": 11131221,
    "Zyptyllic": 11312211,
    "Modyllic": 13122111,
    "Maptyllic": 31212111,
    "Aeraptyllic": 12121113,
    "Katadyllic": 21211131,
    "Magyllic": 12111312,
    "Phrylyllic": 21113121,
    "Epigyllic": 11131212,
    "Molyllic": 11312121,
    "Ponyllic": 13121211,
    "Thyptyllic": 31211211,
    "Ionogyllic": 12112113,
    "Aeolaryllic": 21121131,
    "Katygyllic": 11211312,
    "Ganyllic": 12113121,
    "Kyptyllic": 21131211,
    "Salyllic": 11312112,
    "Sanyllic": 13121121,
    "Doptyllic": 31211121,
    "Ionilyllic": 12111213,
    "Manyllic": 21112131,
    "Polyllic": 11121312,
    "Stanyllic": 11213121,
    "Mixotharyllic": 12131211,
    "Eporyllic": 21312111,
    "Aerynyllic": 13121112,
    "Lonyllic": 31121121,
    "Sathyllic": 11211213,
    "Layllic": 12112131,
    "Saryllic": 21121311,
    "Thacryllic": 11213112,
    "Aeolynyllic": 12131121,
    "Thadyllic": 21311211,
    "Lynyllic": 13112112,
    "Aeolathyllic": 31112121,
    "Aeolocryllic": 11121213,
    "Phroptyllic": 11212131,
    "Kodyllic": 12121311,
    "Epaptyllic": 21213111,
    "Ionoyllic": 12131112,
    "Gyptyllic": 21311121,
    "Aerythyllic": 13111212,
    "Zagyllic": 31112112,
    "Epacryllic": 11121123,
    "Thorcryllic": 11211231,
    "Loptyllic": 12112311,
    "Katylyllic": 21123111,
    "Malyllic": 11231112,
    "Mydyllic": 12311121,
    "Thycryllic": 23111211,
    "Gythyllic": 31111221,
    "Pyryllic": 11112213,
    "Rycryllic": 11122131,
    "Phrathyllic": 11221311,
    "Badyllic": 12213111,
    "Phrocryllic": 22131111,
    "Staryllic": 21311112,
    "Zothyllic": 13111122,
    "Tharyllic": 31111212,
    "Sylyllic": 11112123,
    "Lothyllic": 11121231,
    "Daryllic": 11212311,
    "Monyllic": 12123111,
    "Styryllic": 21231111,
    "Aeolacryllic": 12311112,
    "Raptyllic": 23111121,
    "Kataryllic": 31111122,
    "Aerocryllic": 11111223,
    "Zanyllic": 11112231,
    "Aeolonyllic": 11122311,
    "Aeonyllic": 11223111,
    "Kyryllic": 12231111,
    "Sythyllic": 22311111,
    "Katycryllic": 23111112,
    "Stogyllic": 22121211,
    "Ionidyllic": 21212112,
    "Stonyllic": 12121122,
    "Stalyllic": 21211221,
    "Poryllic": 12112212,
    "Mocryllic": 21122121,
    "Aeolyryllic": 11221212,
    "Baryllic": 12212121,
    "Dalyllic": 22112121,
    "Ionyphyllic": 21121212,
    "Zaptyllic": 11212122,
    "Garyllic": 12121221,
    "Gathyllic": 21212211,
    "Mixopyryllic": 12122112,
    "Ionacryllic": 21221121,
    "Stylyllic": 12211212,
    "Stycryllic": 42111111,
    "Ionothyllic": 21111114,
    "Mythyllic": 11111142,
    "Aerylyllic": 11111421,
    "Bonyllic": 11114211,
    "Tholyllic": 11142111,
    "Katyryllic": 11421111,
    "Sadyllic": 14211111,
    "Stolyllic": 41111112,
    "Logyllic": 11111124,
    "Dacryllic": 11111241,
    "Thynyllic": 11112411,
    "Gydyllic": 11124111,
    "Eparyllic": 11241111,
    "Dynyllic": 12411111,
    "Ionyllic": 24111111,
    "Zaryllic": 33111111,
    "Dythyllic": 31111113,
    "Ionaryllic": 11111133,
    "Laryllic": 11111331,
    "Kataptyllic": 11113311,
    "Sonyllic": 11133111,
    "Pathyllic": 11331111,
    "Loryllic": 13311111,
    "Aeronyllic": 32111121,
    "Pycryllic": 21111213,
    "Mygyllic": 11112132,
    "Lylyllic": 11121321,
    "Daptyllic": 11213211,
    "Ioninyllic": 12132111,
    "Epaphyllic": 21321111,
    "Lolyllic": 13211112,
    "Stacryllic": 31211112,
    "Doryllic": 12111123,
    "Kadyllic": 21111231,
    "Rynyllic": 11112312,
    "Aerogyllic": 11123121,
    "Rothyllic": 11231211,
    "Kagyllic": 12312111,
    "Stathyllic": 23121111,
    "Thyryllic": 22221111,
    "Gygyllic": 22211112,
    "Sodyllic": 22111122,
    "Goryllic": 21111222,
    "Bothyllic": 11112222,
    "Gynyllic": 11122221,
    "Ionaptyllic": 11222211,
    "Phryryllic": 12222111,
    "Racryllic": 22211211,
    "Epicryllic": 22112112,
    "Stygyllic": 21121122,
    "Syryllic": 11211222,
    "Stythyllic": 12112221,
    "Aerothyllic": 21122211,
    "Mixoryllic": 11222112,
    "Thanyllic": 12221121,
    "Roryllic": 22112211,
    "Epotyllic": 21122112,
    "Epidyllic": 11221122,
    "Kaptyllic": 12211221,
    "MajorDimin.": 21212121,
    "MinorDimin.": 12121212,
    "Aerycrygic": 221112111,
    "Gadygic": 211121112,
    "Solygic": 111211122,
    "Zylygic": 112111221,
    "Garygic": 121112211,
    "Sorygic": 211122111,
    "Godygic": 111221112,
    "Epithygic": 112211121,
    "Ionoptygic": 122111211,
    "Kalygic": 311211111,
    "Ionodygic": 112111113,
    "Bythygic": 121111131,
    "Epygic": 211111311,
    "Marygic": 111113112,
    "Gaptygic": 111131121,
    "Aeroptygic": 111311211,
    "Mylygic": 113112111,
    "Galygic": 131121111,
    "Mixolydygic": 311121111,
    "Ionycrygic": 111211113,
    "Zoptygic": 112111131,
    "Phrygygic": 121111311,
    "Locrygic": 211113111,
    "Gonygic": 111131112,
    "Aeracrygic": 111311121,
    "Aerathygic": 113111211,
    "Dorygic": 131112111,
    "Dycrygic": 311112111,
    "Aeolygic": 111121113,
    "Dydygic": 111211131,
    "Tholygic": 112111311,
    "Rynygic": 121113111,
    "Bycrygic": 211131111,
    "Zacrygic": 111311112,
    "Panygic": 113111121,
    "Dyrygic": 131111211,
    "Loptygic": 311111211,
    "Katylygic": 111112113,
    "Phradygic": 111121131,
    "Mixodygic": 111211311,
    "Katalygic": 112113111,
    "Katorygic": 121131111,
    "Dogygic": 211311111,
    "Zodygic": 113111112,
    "Madygic": 131111121,
    "Bagygic": 221211111,
    "Mathygic": 212111112,
    "Styptygic": 121111122,
    "Zolygic": 211111221,
    "Sydygic": 111112212,
    "Katygic": 111122121,
    "Zyphygic": 111221211,
    "Aeralygic": 112212111,
    "Ryptygic": 122121111,
    "Apinygic": 221111121,
    "Katagygic": 211111212,
    "Radygic": 111112122,
    "Gothygic": 111121221,
    "Lythygic": 111212211,
    "Bacrygic": 112122111,
    "Aerygic": 121221111,
    "Dathygic": 212211111,
    "Boptygic": 122111112,
    "Epyrygic": 212112111,
    "Aeradygic": 121121112,
    "Staptygic": 211211121,
    "Danygic": 112111212,
    "Goptygic": 121112121,
    "Epocrygic": 211121211,
    "Rocrygic": 111212112,
    "Zyrygic": 112121121,
    "Sadygic": 121211211,
    "Aeolorygic": 212111211,
    "Thydygic": 121112112,
    "Gycrygic": 211121121,
    "Lyrygic": 111211212,
    "Modygic": 112112121,
    "Katodygic": 121121211,
    "Moptygic": 211212111,
    "Ionocrygic": 112121112,
    "Gocrygic": 121211121,
    "Manygic": 411111111,
    "Polygic": 111111114,
    "Stanygic": 111111141,
    "Thaptygic": 111111411,
    "Eporygic": 111114111,
    "Aerynygic": 111141111,
    "Thyptygic": 111411111,
    "Ionogygic": 114111111,
    "Aeolarygic": 141111111,
    "Sathygic": 321111111,
    "Ladygic": 211111113,
    "Sarygic": 111111132,
    "Thacrygic": 111111321,
    "Aeolynygic": 111113211,
    "Thadygic": 111132111,
    "Lynygic": 111321111,
    "Doptygic": 113211111,
    "Ionilygic": 132111111,
    "Phrygic": 312111111,
    "Aeranygic": 121111113,
    "Dothygic": 211111131,
    "Lydygic": 111111312,
    "Stadygic": 111113121,
    "Byptygic": 111131211,
    "Stodygic": 111312111,
    "Zynygic": 113121111,
    "Lonygic": 131211111,
    "Zothygic": 311111121,
    "Aeolathygic": 111111213,
    "Aeolocrygic": 111112131,
    "Phroptygic": 111121311,
    "Kodygic": 111213111,
    "Eparygic": 112131111,
    "Ionygic": 121311111,
    "Gyptygic": 213111111,
    "Aerythygic": 131111112,
    "Aeolacrygic": 311111112,
    "Raptygic": 111111123,
    "Gythygic": 111111231,
    "Pyrygic": 111112311,
    "Rycrygic": 111123111,
    "Phrathygic": 111231111,
    "Badygic": 112311111,
    "Phrocrygic": 123111111,
    "Starygic": 231111111,
    "Kyrygic": 222111111,
    "Sythygic": 221111112,
    "Katycrygic": 211111122,
    "Tharygic": 111111222,
    "Sylygic": 111112221,
    "Lothygic": 111122211,
    "Darygic": 111222111,
    "Monygic": 112221111,
    "Styrygic": 122211111,
    "Porygic": 221121111,
    "Mocrygic": 211211112,
    "Aeolyrygic": 112111122,
    "Barygic": 121111221,
    "Katarygic": 211112211,
    "Aerocrygic": 111122112,
    "Zanygic": 111221121,
    "Aeolonygic": 112211211,
    "Aeolanygic": 122112111,
    "Kaptygic": 221111211,
    "Sacrygic": 211112112,
    "Padygic": 111121122,
    "Epilygic": 111211221,
    "Kynygic": 112112211,
    "Stophygic": 121122111,
    "Ionidygic": 211221111,
    "Stonygic": 112211112,
    "Stalygic": 122111121,
    "Koptygic": 212121111,
    "Raphygic": 121211112,
    "Zycrygic": 212111121,
    "Mycrygic": 121111212,
    "Laptygic": 211112121,
    "Pylygic": 111121212,
    "Rodygic": 111212121,
    "Epolygic": 112121211,
    "Epidygic": 121212111,
    "Phronygic": 211211211,
    "Stynygic": 112112112,
    "Zydygic": 121121121,
    "Aerycryllian": 2111211111,
    "Gadyllian": 1112111112,
    "Solyllian": 1121111121,
    "Zyphyllian": 1211111211,
    "Garyllian": 2111112111,
    "Soryllian": 1111121112,
    "Godyllian": 1111211121,
    "Epityllian": 1112111211,
    "Ionyllian": 1121112111,
    "Aeoryllian": 1211121111,
    "Katoryllian": 3111111111,
    "Dodyllian": 1111111113,
    "Zogyllian": 1111111131,
    "Madyllian": 1111111311,
    "Dycryllian": 1111113111,
    "Aeogyllian": 1111131111,
    "Dydyllian": 1111311111,
    "Thogyllian": 1113111111,
    "Rygyllian": 1131111111,
    "Bathyllian": 1311111111,
    "Sydyllian": 2211111111,
    "Katogyllian": 2111111112,
    "Mixodyllian": 1111111122,
    "Aeradyllian": 1111111221,
    "Ryptyllian": 1111112211,
    "Loptyllian": 1111122111,
    "Kataphyllian": 1111221111,
    "Phradyllian": 1112211111,
    "Dagyllian": 1122111111,
    "Katyllian": 1221111111,
    "Gothyllian": 2121111111,
    "Lythyllian": 1211111112,
    "Bacryllian": 2111111121,
    "Aerygyllian": 1111111212,
    "Dathyllian": 1111112121,
    "Boptyllian": 1111121211,
    "Bagyllian": 1111212111,
    "Mathyllian": 1112121111,
    "Styptyllian": 1121211111,
    "Zolyllian": 1212111111,
    "Staptyllian": 2112111111,
    "Danyllian": 1121111112,
    "Goptyllian": 1211111121,
    "Epocryllian": 2111111211,
    "Rocryllian": 1111112112,
    "Zyryllian": 1111121121,
    "Sagyllian": 1111211211,
    "Epinyllian": 1112112111,
    "Katagyllian": 1121121111,
    "Ragyllian": 1211211111,
    "Thydyllian": 2111121111,
    "Epiryllian": 1111211112,
    "Lyryllian": 1112111121,
    "Mogyllian": 1121111211,
    "Katodyllian": 1211112111,
    "Aerycratic": 21111111111,
    "Monatic": 11111111112,
    "Solatic": 11111111121,
    "Zylatic": 11111111211,
    "Mixolatic": 11111112111,
    "Soratic": 11111121111,
    "Godatic": 11111211111,
    "Eptatic": 11112111111,
    "Ionatic": 11121111111,
    "Aeolatic": 11211111111,
    "Thydatic": 12111111111,
    "Chromatic": 111111111111,
}

def get_scale(name: str) -> list:
    """Get a scale from the global scale list"""
    scale = SCALES.get(
        name.lower().capitalize(),
        SCALES["Chromatic"])
    return list(map(int, str(scale)))

if __name__ == "__main__":
    print(get_scale("Godatic"))
