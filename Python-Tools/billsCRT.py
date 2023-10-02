from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto import Random
import Crypto
import sys
import libnum
#This can be done with at minimum 3 values of each n and c
n1=12426348204210593270343924563278821305386892683425418957350363905840484905896816630189546938112358425679727243103082954824537007026886458498690134225705484501535835385800730412220192564706251228021192115494699150390312107794005569764411063907390563937247515046052549753641884721864426154021041082461015103337120756347692245843318676049947569653604616584167536958803278688355036036887022591104659059883622072052793378468850702811804337808760402077376453702190206077039468600466511349923882037572540505571672225260106649075841827340894515208811788428239691505001675042096850318994923571686175381862745049100863883977473
n2=19928073532667002674271126242460424264678302463110874370548818138542019092428748404842979311103440183470341730391245820461360581989271804887458051852613435204857098017249255006951581790650329570721461311276897625064269097611296994752278236116594018565111511706468113995740555227723579333780825133947488456834006391113674719045468317242000478209048237262125983164844808938206933531765230386987211125968246026721916610034981306385276396371953013685639581894384852327010462345466019070637326891690322855254242653309376909918630162231006323084408189767751387637751885504520154800908122596020421247199812233589471220112129
n3=13985338100073848499962346750699011512326742990711979583786294844886470425669389469764474043289963969088280475141324734604981276497038537100708836322845411656572006418427866013918729379798636491260028396348617844015862841979175195453570117422353716544166507768864242921758225721278003979256590348823935697123804897560450268775282548700587951487598672539626282196784513553910086002350034101793371250490240347953205377022300063974640289625028728548078378424148385027286992809999596692826238954331923568004396053037776447946561133762767800447991022277806874834150264326754308297071271019402461938938062378926442519736239
n4=19594695114938628314229388830603768544844132388459850777761001630275366893884362012318651705573995962720323983057152055387059580452986042765567426880931775302981922724052340073927578619711314305880220746467095847890382386552455126586101506301413099830377279091457182155755872971840333906012240683526684419808580343325425793078160255607072901213979561554799496270708954359438916048029174155327818898336335540262711330304350220907460431976899556849537752397478305745520053275803008830388002531739866400985634978857874446527750647566158509254171939570515941307939440401043123899494711660946335200589223377770449028735883
n5=12091176521446155371204073404889525876314588332922377487429571547758084816238235861014745356614376156383931349803571788181930149440902327788407963355833344633600023056350033929156610144317430277928585033022575359124565125831690297194603671159111264262415101279175084559556136660680378784536991429981314493539364539693532779328875047664128106745970757842693549568630897393185902686036462324740537748985174226434204877493901859632719320905214814513984041502139355907636120026375145132423688329342458126031078786420472123904754125728860419063694343614392723677636114665080333174626159191829467627600232520864728015961207
n6=19121666910896626046955740146145445167107966318588247850703213187413786998275793199086039214034176975548304646377239346659251146907978120368785564098586810434787236158559918254406674657325596697756783544837638305550511428490013226728316473496958326626971971356583273462837171624519736741863228128961806679762818157523548909347743452236866043900099524145710863666750741485246383193807923839936945961137020344124667295617255208668901346925121844295216273758788088883216826744526129511322932544118330627352733356335573936803659208844366689011709371897472708945066317041109550737511825722041213430818433084278617562166603
n7=13418736740762596973104019538568029846047274590543735090579226390035444037972048475994990493901009703925021840496230977791241064367082248745077884860140229573097744846674464511874248586781278724368902508880232550363196125332007334060198960815141256160428342285352881398476991478501510315021684774636980366078533981139486237599681094475934234215605394201283718335229148367719703118256598858595776777681347337593280391052515991784851827621657319164805164988688658013761897959597961647960373018373955633439309271548748272976729429847477342667875183958981069315601906664672096776841682438185369260273501519542893405128843
n8=11464859840071386874187998795181332312728074122716799062981080421188915868236220735190397594058648588181928124991332518259177909372407829352545954794824083851124711687829216475448282589408362385114764290346196664002188337713751542277587753067638161636766297892811393667196988094100002752743054021009539962054210885806506140497869746682404059274443570436700825435628817817426475943873865847012459799284263343211713809567841907491474908123827229392305117614651611218712810815944801398564599148842933378612548977451706147596637225675719651726550873391280782279097513569748332831819616926344025355682272270297510077861213
n9=21079224330416020275858215994125438409920350750828528428653429418050688406373438072692061033602698683604056177670991486330201941071320198633550189417515090152728909334196025991131427459901311579710493651699048138078456234816053539436726503461851093677741327645208285078711019158565296646858341000160387962592778531522953839934806024839570625179579537606629110275080930433458691144426869886809362780063401674963129711723354189327628731665487157177939180982782708601880309816267314061257447780050575935843160596133370063252618488779123249496279022306973156821343257109347328064771311662968182821013519854248157720756807
n10=22748076750931308662769068253035543469890821090685595609386711982925559973042348231161108618506912807763679729371432513862439311860465982816329852242689917043600909866228033526990181831690460395726449921264612636634984917361596257010708960150801970337017805161196692131098507198455206977607347463663083559561805065823088182032466514286002822511854823747204286303638719961067031142962653536148315879123067183501832837303731109779836127520626791254669462630052241934836308543513534520718206756591694480011760892620054163997231711364648699030108110266218981661196887739673466188945869132403569916138510676165684240183111
n11=15211900116336803732344592760922834443004765970450412208051966274826597749339532765578227573197330047059803101270880541680131550958687802954888961705393956657868884907645785512376642155308131397402701603803647441382916842882492267325851662873923175266777876985133649576647380094088801184772276271073029416994360658165050186847216039014659638983362906789271549086709185037174653379771757424215077386429302561993072709052028024252377809234900540361220738390360903961813364846209443618751828783578017709045913739617558501570814103979018207946181754875575107735276643521299439085628980402142940293152962612204167653199743
n12=21920948973299458738045404295160882862610665825700737053514340871547874723791019039542757481917797517039141169591479170760066013081713286922088845787806782581624491712703646267369882590955000373469325726427872935253365913397944180186654880845126957303205539301069768887632145154046359203259250404468218889221182463744409114758635646234714383982460599605335789047488578641238793390948534816976338377433533003184622991479234157434691635609833437336353417201442828968447500119160169653140572098207587349003837774078136718264889636544528530809416097955593693611757015411563969513158773239516267786736491123281163075118193
c1=5065488652323342174251548936130018278628515304559137485528400780060697119682927936946069625772269234638180036633146283242714689277793018059046463458498115311853401434289264038408827377579534270489217094049453933816452196508276029690068611901872786195723358744119490651499187556193711866091991489262948739533990000464588752544599393
c2=86893891006724995283854813014390877172735163869036169496565461737741926829273252426484138905500712279566881578262823696620415864916590651557711035982810690227377784525466265776922625254135896966472905776613722370871107640819140591627040592402867504449339363559108090452141753194477174987394954897424151839006206598186417617292433784471465084923195909989
c3=86893891006724995283854813014390877172735163869036169496565461737741926829273252426484138905500712279566881578262823696620415864916590651557711035982810690227377784525466265776922625254135896966472905776613722370871107640819140591627040592402867504449339363559108090452141753194477174987394954897424151839006206598186417617292433784471465084923195909989
c4=5065488652323342174251548936130018278628515304559137485528400780060697119682927936946069625772269234638180036633146283242714689277793018059046463458498115311853401434289264038408827377579534270489217094049453933816452196508276029690068611901872786195723358744119490651499187556193711866091991489262948739533990000464588752544599393
c5=301927034179130315172951479434750678833634853032331571873622664841337454556713005601858152523700291841415874274186191308636935232309742600657257783870282807784519336918511713958804608229440141151963841588389502276162366733982719267670094167338480873020791643860930493832853048467543729024717103511475500012196697609001154401
c6=38999477927573480744724357594313956376612559501982863881503907194813646795174312444340693051072410232762895994061399222849450325021561935979706475527169503326744567478138877010606365500800690273
c7=38999477927573480744724357594313956376612559501982863881503907194813646795174312444340693051072410232762895994061399222849450325021561935979706475527169503326744567478138877010606365500800690273
c8=38999477927573480744724357594313956376612559501982863881503907194813646795174312444340693051072410232762895994061399222849450325021561935979706475527169503326744567478138877010606365500800690273
c9=301927034179130315172951479434750678833634853032331571873622664841337454556713005601858152523700291841415874274186191308636935232309742600657257783870282807784519336918511713958804608229440141151963841588389502276162366733982719267670094167338480873020791643860930493832853048467543729024717103511475500012196697609001154401
c10=5065488652323342174251548936130018278628515304559137485528400780060697119682927936946069625772269234638180036633146283242714689277793018059046463458498115311853401434289264038408827377579534270489217094049453933816452196508276029690068611901872786195723358744119490651499187556193711866091991489262948739533990000464588752544599393
c11=301927034179130315172951479434750678833634853032331571873622664841337454556713005601858152523700291841415874274186191308636935232309742600657257783870282807784519336918511713958804608229440141151963841588389502276162366733982719267670094167338480873020791643860930493832853048467543729024717103511475500012196697609001154401
c12=86893891006724995283854813014390877172735163869036169496565461737741926829273252426484138905500712279566881578262823696620415864916590651557711035982810690227377784525466265776922625254135896966472905776613722370871107640819140591627040592402867504449339363559108090452141753194477174987394954897424151839006206598186417617292433784471465084923195909989

if (len(sys.argv)>1):
    c1=int(sys.argv[1])
if (len(sys.argv)>2):
    c2=int(sys.argv[2])
if (len(sys.argv)>3):
    c3=int(sys.argv[3])
if (len(sys.argv)>4):
    n1=int(sys.argv[4])
if (len(sys.argv)>5):
    n2=int(sys.argv[5])
if (len(sys.argv)>6):
    n3=int(sys.argv[6])                
e=3



mod=[n1,n2,n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]
rem=[c1,c2,c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]

res=libnum.solve_crt(rem[:3],mod[:3])

print("\n\nAnswer:")
print(f"\nCipher 1: {c1}, N1={n1}")
print(f"Cipher 2: {c2}, N2={n2}")
print(f"Cipher 3: {c3}, N3={n3}")


print(f"\nWe can solve M^e with CRT to get {res}")
val=libnum.nroot(res,3)
print(f"\nIf we assume e=3, we take the third root to get: {val}")
print("Next we convert this integer to bytes, and display as a string.")
print(f"\nDecipher: {long_to_bytes(val)}")