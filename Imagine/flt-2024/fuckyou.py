from Crypto.Util.number import inverse, long_to_bytes

# Given values
N = 1211944345258274660554893280872694197873620050992022144118122817680950992370433954845654303411968537072836810997694929664785000718358875494701902392184943678309368575707921212904796945432810323441336651616322470455524238236104234068598504854742977688218122199956237812773377589417125859922878980457216899078882452287292823999820676463878072739876344311613999418319286598436084975209546457119806983102138468859681691803656968913399196451724459596202552118110723411374442696302805727498713308187366881649725520048444537232818388575199314346000014201860467139897376001935786431665335199666545075563010737625335193
e = 1926243667084634739203147690812942502525097290856569053657671536655703493289225750756096924038107005577607033307665468424208137938409502571528443836358087248839788279968559509024035796546319252657655336760524962441730035462535605201830750366358528761302330842735547127895806782933537114179584526963468216986770292126516600991528330730591092675617705347259421471242773870189847123188284654268637811712275571627971148712543359837388894030588963383698683834864693119003005366606165183170149153573926170079092892562190097447338461713096678175819845507525768121215319760765625810900051503098306187879655114031496361
c = 502906972015000551965005087652753757140464925808007805272195926148666055392302276728236863942643450123085116965066916224940561509266449290365566972775823931044723201558938980801794978456855187924431761988738656089487364751051998096559567741403742226862245955167297065928788092159665524622315023631657582963455126703371709572254632471774928660993076296134126774467136423741633174538812022517694524327174708807298314709693218661937232278658205499019216148414432841342209718613058924755791471023996723502052594984620733306156667078964155491062072814052918669166902679354900648008286908546493975052586610697551811

# Calculate the private exponent d
phi_N = N - 1
d = inverse(e, phi_N)

# Decrypt the ciphertext
m = pow(c, d, N)
flag = long_to_bytes(m)

print("Decrypted Flag:", flag)
