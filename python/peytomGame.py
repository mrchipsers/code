
#WORDLE GAME
#TESTING THE COLORS: print("\033[92mHello \033[91mWorld \033[93mPeyton \033[0m") ##Green Hello, Red World, Yellow Peyton, \033[0m Black

import random

def main():
	difficulty = start_screen()
	word, guesses_left = choose_answer(difficulty)
	validate_display(word, guesses_left)

def start_screen():
	print('\n-------- WELCOME TO \033[91mW\033[93mO\033[92mR\033[91mD\033[93mL\033[92mE\033[0m --------\n')
	difficulty = 0
	while difficulty not in ['1','2','3']:
		difficulty = input('What difficulty would you like to play? Easy(1), Medium(2), Hard(3): ')
	if difficulty == '1':
		print('INSTRUCTIONS:\nYou have chosen EASY mode. You will have a word with 5 letters and 8 guesses.\nIf the letter is \033[92mGREEN \033[0m then the letter is in the right spot.\nIf the letter is \033[93mYELLOW \033[0m then it is in the word with in the wrong spot. \nIf the letter is \033[91mRED \033[0m then it is not in the word.')
	elif difficulty == '2':
		print('INSTRUCTIONS:\nYou have chosen MEDIUM mode. You will have a word with 6 letters and 7 guesses.\nIf the letter is \033[92mGREEN \033[0m then the letter is in the right spot.\nIf the letter is \033[93mYELLOW \033[0m then it is in the word with in the wrong spot. \nIf the letter is \033[91mRED \033[0m then it is not in the word.')
	else:		
		print('INSTRUCTIONS:\nYou have chosen HARD mode. You will have a word with 7 letters and 6 guesses.\nIf the letter is \033[92mGREEN \033[0m then the letter is in the right spot.\nIf the letter is \033[93mYELLOW \033[0m then it is in the word with in the wrong spot. \nIf the letter is \033[91mRED \033[0m then it is not in the word.')
	print('GOODLUCK!\n')
	return difficulty

def choose_answer(difficulty):
	word5 = ['abode','above','aches', 'acres', 'adept','agony', 'ahead','aisle','album','alias','align','allow','alarm','aloft','along','alpha','alone','aloud','anvil','ankle','apron',
'aroma','array','avoid','avert','awake','awful','ashes','arrow','annoy','argue','anime','annex','angst','alien','alive','acorn','baggy','bacon','bagel','badly','banal','basic','batch','basil'
,'beast','beard','beats','beach','beams','begun','beige','below','bible','bicep','biome','birch','blaze','bleed','bless','bleak','blood','bluff','bloom','bonus','braid','brave','boxer',
'brawl','bunny','cacao','cabin','cameo','camel','canoe','carve','cater','candy','canon','cargo','cello','cedar','chart','chant','cheat','chasm','cheif','chili','child','chick','chuck',
'chore','cigar','clasp','climb','cliff','clown','clock','cloth','coach','colon','condo','comic','comfy','cough','craft','crank','creep','crawl','cycle','curve','crime','daily','daisy','dairy'
,'dance','death','decor','daddy','debit','dealt','delay','delta','demon','detox','devil','deity','debug','diary','dirty','dizzy','digit','dough','dozen','drain','drawn','drama','drink',
'drift','dying','dusty','drool','elder','elbow','early','emoji','eject','enjoy','enter','erase','erupt','equip','ethic','event','exist','extra','error','equal','essay','epoxy','faint','faith'
,'favor','fatal','fairy','false','fever','fence','fiels','fifty','final','fight','fiery','flame','fleas','flask','flies','flirt','floar','flunk','fluff','fudge','fries','funny','furry',
'fungi','fuzzy','gamer','gavel','geeky','geese','genre','girth','glaze','glint','globe','glory','gloom','glide','goose','grain','graph','grasp','green','grape','groom','guest','guard','gummy'
,'habit','hairy','harsh','haven','haiky','halal','heard','havoc','happy','hardy','heavy','hefty','hello','hippo','hobby','holly','horse','human','humus','humid','hyper',
'icing','ideal','idiot','idiom','inbox','imply','index','indie','ionic','irony','intro','ivory','issue','igloo','itchy','jelly','jewel','joker'
,'jolly','juice','jumbo','jewel','jeans','jerky','judge','kitty','kirby','knee','knack','koala','knife','kiddo','kayak','kiosk','label','labour',
'large','latex','laugh','latte','lathe','laser','leash','leech','legal','legit','level','lilac','lingo','limbo','local','loose','lover','loyal',
'lucis','lyric','lunge','magic','mango','manga','march','maple','manic','match','mayor','medic','maybe','media','melon','merge','merry','metro',
'mirco','minty','minor','mixer','mocha','model','moist','moron','moose','morph','motor','motel','music','mushy','nacho','nasty','needy','nerve',
'niche','never','nifty','ninja','noise','noose','notch','nosey','nylon','novel','notes','nurse','oasis','obese','olive','older','opera','ombre',
'organ','orbit','otter','other','ounce','owner','ozone','oxide','paint','pagan','parka','pasta','party','patio','patch','peace','peach','pearl'
,'pecan','peril','photo','piano','phone','pilot','pinky','pivol','pixel','pizza','pinch','plate','polar','poker','porch','power','prank','pride',
'prize','pupil','purge','puffy','quail','quark','query','quote','quota','queen','queue','quiet','quest','rabbi','rabid','radio','ramen','ranch',
'ratio','razor','ready','rebel','rainy','reels','relic','renew','resin','reset','repay','rhino','right','risky','rinse','roach','robot','rogue',
'route','royal','round','roough','rural','rusty','saint','salad','sauce','salon','sauna','savvy','scent','scary','scoop','scope','score','scare',
'sense','serve','setup','seven','sharp','shelf','sheep','shift','shirt','shrug','sigma','skill','skate','sleep','slope','sloth','slush','smirk',
'small','smoke','snipe','snake','snoop','sonic','speed','spell','spice','spill','spoon','squid','staff','stall','steak','stick','stool','storm',
'story','style','surge','sugar','swipe','swirl','table','tacos','taboo','tarot','talon','tasty','taxes','teddy','teeth','tenor','tempo','theme',
'theft','thick','think','thing','thumb','timid','timer','tired','tonic','toast','torch','toxin','towel','trade','treat','trick','troll','trunk',
'truck','tulip','twirl','typos','twice','twist','udder','unzip','usher','using','ultra','union','upper','until','under','urban','uncle','vibes','vegan','valid','vinyl','vivid','voice','vowel','vomit','virus','villa','vogue','wacky','wafer','wagon','waltz','weigh','wedge','wheel',
'wheat','whale','which','widow','whisk','white','witch','world','wooly','women','write','wrong','wrist','worth','yacht','yahoo','yield','youth',
'yummy','yearn','zebra','zesty']

	word6 = ['aboard','absent','abrupt','absurd','accent','action','adored','addict','active','affirm','agency','aliens','almond','almost',
'alumni','amount','analog','animal','answer','annual','anthem','anyone','anyhow','arcade','around','armour','arrest','asleep','artist','aspect'
,'astral','atomic','attack','avenue','august','attest','bagels','bakery','bamboo','ballet','banana','barbie','barley','barrow','basalt','basket'
,'batman','beauty','beaver','beacon','beauty','belief','beware','better','bikini','binary','bitter','bishop','bleach','blonde','boogie','borrow',
'bottom','branch','breath','bridge','browse','bronze','bubble','bullet','burden','button','butler','buzzer','butter','cactus','calmer','cancer',
'candle','cancel','cannon','canvas','canine','canyon','career','cardio','carbon','carrot','cartel','casket','cattle','celery','cellar','center',
'cereal','chapel','cheese','chilli','choice','chrome','chorus','cinema','citrus','cliche','clinic','closet','coffee','coding','cocoon','column',
'common','commit','copper','corpse','couple','coupon','cousin','create','cringe','crisis','critic','crunch','cruise','crypto','cuddle','custom',
'cyborg','dagger','danger','damage','dating','debate','decade','decode','deduct','define','defeat','delete','desert','design','detail','dinner',
'doctor','donkey','doodle','domino','double','driver','dragon','duplex','during','eagles','earthy','editor','edible','effect','eleven','encore',
'engage','energy','enlist','enroll','erased','estate','ethnic','evolve','eureka','except','exotic','expert','expire','expose','export','eyelid',
'fabric','factor','falcon','family','fandom','father','fathom','favour','fellow','feline','felony','female','fiance','fields','fiesta','figure',
'finale','finish','fleece','flavor','flower','flight','forget','forgot','formal','fossil','freaky','french','frozen','fruity','future','galaxy',
'gambit','garage','garlic','garden','genius','gentle','giggle','ginger','glazed','glitch','gloomy','global','goalie','goblin','google','golden',
'gossip','gravel','greedy','groovy','ground','growth','grunge','guilty','guinea','gutter','hammer','happen','hangar','handle','harbor','hating',
'health','heaven','heated','herbal','hermit','heroic','highly','hockey','hollow','honest','horror','hostel','hornet','hunger','hunter','hurdle',
'hustle','iconic','ignite','ignore','impact','improv','import','indigo','income','infant','inform','injury','insane','insect','insert','inside',
'insult','invite','intern','iodine','island','itself','jacked','jacket','joyful','jersey','junior','jigsaw','jockey','jingle','karate','kennel',
'killer','kitten','kinder','kidney','keeper','kosher','kindle','kidnap','ladder','laptop','launch','layout','leader','leaned','ledger','larger',
'lagoon','legend','legacy','lesson','liable','length','likely','lineup','linear','liquid','linger','little','lizard','loaded','lotion','louder',
'longer','loudly','lovely','lounge','luxury','lumbar','magnet','makeup','mammal','manage','mantle','manure','manual','marble','margin','maroon',
'market','mashed','marvel','martyr','mascot','maniac','mantra','matrix','mature','median','median','melted','memoir','member','memory','mentor',
'meteor','minion','mirage','misuse','modify','moment','monkey','morbid','morale','mosaic','motive','motion','museum','murder','mutant','mythic',
'mutton','napkin','nation','nature','nausea','nectar','nearly','neuron','nickel','normal','novice','notion','nobody','nugget','number','nutmeg',
'object','offend','office','occupy','obtain','online','opaque','oracle','orchid','option','origin','orphan','outage','outfit','outlet','output',
'oxygen','oyster','paddle','palace','palate','pantry','parade','parent','parole','pardon','parlor','parrot','partly','parody','pastel','patent',
'pastor','peanut','payoff','peaked','patron','pebble','pellet','pencil','permit','period','person','pepper','phobia','photon','pickle','pigeon',
'pistol','piston','pirate','plague','planet','player','plural','pocket','podium','poetic','poison','police','polite','poorly','poodle','potato',
'potent','potion','prayer','pretty','prince','profit','prison','priest','psycho','puddle','public','punish','puzzle','python','purple','quaint',
'quarry','quinoa','quirku','quartz','rabbit','radius','raisin','raptor','rascal','ration','rattle','ravine','random','rabies','really','recall',
'redeem','record','recess','refill','reduce','region','rejoin','relief','relish','reamin','remedy','remind','remote','replay','repeat','report',
'resort','resume','retail','result','review','ribbon','riddle','ripple','ritual','robust','rocket','rodent','rotten','royale','rubber','rustic',
'rowing','saddle','sailor','safari','salary','savage','scarce','scared','savage','salmon','scheme','saloon','sanity','sample','scotch','screen',
'script','scroll','season','search','second','secret','secure','selfie','seller','senior','select','serial','sermon','sesame','sweage','shadow',
'sewing','sharif','shiver','shield','should','shower','shrimp','shrine','silent','signal','simmer','sinful','sister','sitter','sitcom','sketch',
'skinny','skiing','slider','slight','sloppy','slower','smooth','smokey','snitch','sneaky','soacked','social','sniper','softer','solemn','sooner',
'speech','speedy','spider','spiced','spinal','sponge','spooky','spouse','squirt','stable','stanze','staple','status','statue','stereo','sticky',
'stinky','stitch','stolen','stormy','street','stress','streak','stream','strict','strong','studio','stuffy','stroke','stupid','subtle','submit',
'subway','sulfur','sunset','summon','supper','survey','sweaty','symbol','switch','tablet','taller','tanker','tavern','tattoo','tavern','taught',
'temple','tenant','temper','tennis','terror','texted','theory','thrift','thrill','thrive','thrown',',throat','ticket','timber','timely','toilet',
'torque','tomato','toward','tissue','tragic','trauma','travel','trophy','trusty','turkey','twitch','tyrant','tycoon','typing','turtle','tunnel',
'tuxedo','umpire','unborn','uneasy','unholy','unless','unreal','unseen','untrue','unwind','unwise','upbeat','unlock','uncles','uptown','urgent',
'update','utopia','urging','upload','upkeep','vacant','valley','vanish','vapour','vanity','vendor','velvet','vector','veggie','versus','verify','victim','cisble','vessel','verbal','victim','violet','viewer','volley','vortex','voyage','volume','vulgar','violin','waffle','waiter',
'warden','wallet','warmth','wasted','weapon','weakly','walnut','wanted','weaver','waiver','weekly','weight','weirdo','wicked','wildly','willow',
'window','winter','wisdom','wizard','wither','wonder','worthy','wrench','wright','wobble','yogurt','yellow','yearly','yelled','zipper','zodiac',
'zombie']

	word7 = ['abandon','abdomen','abolish','abstain','abusive','acidity','acronym','aquire','achieve','acrylic','academy','ability',
'actress','adopted','aerobic','agility','against','advisor','adverse','adapter','advance','adapter','airport','allergy','already','alright',
'allowed','alluded','amateur','amnesia','analogy','analyze','anarchy','analyst','amongst','ammonia','amazing','ancient','another','annoyed',
'animate','antenna','anziety','anxious','anguish','aqueous','arcadia','aquatic','archive','arsenic','asphalt','assault','asprin','artwork',
'atheist','attract','autopsy','argument','average','avocado','awesome','awkward','awfully','avoided','babysit','banking','baptism','barista',
'bassist','bathtub','battled','bayonet','beating','bedroom','bedtime','bedrock','benefit','beneath','bycicle','biggest','bipolar','blazing','blanket','billion','blurred','blossom','bizarre','bonfire','booster','boredom','bouncer','bracket','bracing','braille','bravely','breakup',
'brewery','briefly','brother','brownie','buildup','burrito','buzzing','zutcher','burnout','cabbage','calibre','cabinet','calcium','calming',
'camping','caption','capture','captive','cartoon','carrier','cardiac','carving','caravan','capital','canteen','catalog','cashier','catfish',
'caution','century','ceramic','channel','charger','chapter','chaotic','cheaply','charity','checker','cheddar','chemist','cherish','chicken',
'chewing','cheetah','chipped','chocking','chimney','chronic','clarify','cleanly','closest','slosure','clutter','coaster','coconut','cohorts',
'collins','collide','collect','coldest','comedic','comment','complex','concern','cofess','consent','consist','consult','control','correct','corrupt','cracker','cracked','created','creator','crochet','crucial','cruelty','cryptic','cupcake','culture','custard','cycolone','cycling',
'cyclops','damage','dancing','dealing','darling','decided','decimal','declare','daytime','default','defiant','deflect','delayed','demonic',
'deleted','density','dentist','deposit','deprive','derived','descent','desktop','despair','dessert','develop','devious','deviate','dictate',
'digital','dignity','diploma','dioxide','dislike','disrupt','distort','diverse','dolphin','dodging','drained','drastic','dreamer','draught','drizzle','dropout','dungeon','dumbest','dubset','duchess','dynamic','dynasty','earlier','elderly','embargo','emotion','empathy','ecology',
'educate','eastern','economy','emerald','embassy','eminent','emperor','elevate','enabled','emptied','empower','endgame','enforce','enjoyed',
'entropy','epitome','equally','equinox','erosion','erupted','essence','ethanol','ethical','excited','exhibit','explain','extinct','eyeball',
'eyebrow','faintly','failure','farming','fantasy','fascism','fanatic','faction','fatally','fateful','fatigue','feather','feature','fertile',
'fighter','fiancee','finesse','finally','fireman','firearm','firefly','fission','fixture','flannel','fitness','flavour','flexing','flicker',
'florist','foliage','fooling','forbids','forearm','forgive','forward','fortune','fragile','freedom','freezer','fulfill','frosted','further',
'furious','furnish','gallant','garland','garnish','gateway','gearbox','gentile','generic','genuine','ghastly','giraffe','glacial','glacier',
'glamour','ghostly','gimmick','glucose','goodbye','gorilla','gourmet','gradual','graphic','gravely','grandpa','grammar','gravity','grilled',
'grocery','grizzly','gunfire','gymnast','habitat','haircut','hamster','handbag','hammock','handful','harmony','hateful','hashtag','haunted',
'healthy','hangout','headset','heathen','heavier','heiress','heroine','hideout','history','hideous','hickory','holiday','hostage','however',
'humming','hotline','hygiene','hydrate','iceberg','ideally','idiotic','illness','immoral','imagery','imagine','improve','include','immense',
'inflate','inferno','inhibit','initial','inspect','install','inspire','insulin','intense','invalid','invoice','jackpot','jealous','jewlery',
'journal','jukebox','justice','justify','journey','jumping','karaoke','ketchup','killing','kingdom','knuckle','kissing','kingdom','kitchen',
'kinetic','lactose','laundry','legally','lecture','lawsuit','lasagna','lantern','lattice','leopard','lesbian','lettuce','lexicon','license',
'library','liberal','lightly','lighten','listing','locking','lobster','lottery','loudest','loyalty','lullaby','lyrical','lunatic','luggage',
'luckily','machine','magical','magenta','majesty','manager','manhunt','mandate','mansion','marital','marshal','martian','married','mammoth',
'mailbox','maximum','medical','measure','mediate','medical','melodic','mention','mercury','message','mermaid','messiah','midwife','migrate',
'milking','midterm','mindful','million','mindset','minimum','minivan','missile','missing','mission','mistake','mixtape','mockery','modesty',
'monarch','monitor','monster','morning','musical','mustard','mystery','nervous','newborn','network','natural','neutral','neglect','napping',
'nominee','notable','notable','neither','naughty','nowhere','novelty','nursing','nursery','nonstop','oatmeal','obliged','oblique','oceanic',
'omitted','onboard','optical','officer','ominous','offense','ostrich','organic','outcast','outcome','orderly','outdoor','overdue','overlap',
'outlook','pacific','painful','parable','paradox','paragon','parlous','parsley','partial','partner','partake','parking','pancake','painter',
'panther','pattern','pelican','penguin','pendant','perfect','percent','perform','permits','phantom','pharaoh','phoenix','piccolo','picture','pilgrim','pinball','planter','planner','placebo','plaster','platoon','plateau','plywood','playful','podcast','polygon','popcorn',
'popular','portion','pooping','postage','portray','postman','poverty','powered','poultry','prairie','predict','premier','precise','premise',
'pretend','pretext','prevail','pricing','printer','privacy','proceed','program','profile','promote','propose','protein','proverb','publish',
'purpose','puzzled','pyramid','pronoun','qualify','quality','quantum','quarter','quicker','quoting','quitely','quarrel','raccoon','rainbow',
'rapport','reactor','realise','realism','reality','recital','rebound','reclaim','recycle','rectify','referee','rematch','renewal','replace',
'resolve','roaming','robbery','rivalry','rooftop','roughly','routine','rushing','robotic','saffrom','sadness','scenery','scholar','science',
'seagull','section','seeking','seminar','senator','sensory','serious','setback','session','setting','several','shadowy','shampoo','sheriff',
'shorten','shotgun','shuffle','signify','sincere','silicon','sketchy','skillet','skyline','slender','slavery','slaying','smaller','smarter',
'smiling','snowman','soldier','sorcery','someone','someday','soulful','sparkle','speaker','special','sponsor','squeese','stamina','started',
'stealth','steamed','stomach','stretch','stylish','stylist','subject','succeed','summary','suicide','support','sunrise','surgeon','sweetly',
'synergy','synonym','tactile','tallest','tantrum','teacher','tension','teenage','teacher','tangent','talking','testify','theorem','theatre',
'therapy','thirsty','thermal','through','thunder','tighter','thinker','titanic','tonight','torpedo','totally','tractor','tragedy','tourism',
'torure','traitor','treason','trident','turbine','tuition','turnout','typical','tyranny','twinkle','typhoon','ukulele','unarmed','unequal',
'unhappy','unnamed','upgrade','upscale','unicorn','urgency','utopian','useless','utterly','vacancy','vanilla','various','vampire','vaccine',
'vibrate','vinegar','village','vintage','victory','vibrant','virtual','vehicle','vulture','vitamin','volcano','vividly','waiting','warship',
'website','wealthy','weekday','weirder','warmest','weather','welcome','welding','wetland','welfare','wheeler','whisper','wildca','willful',
'winding','without','wishful','worldly','worship','wrapper','wrongly','written','younger','yielded','yelling','yawning','zoology']

	if difficulty == '1':
		word = random.choice(word5)
		guesses_left = 8
	elif difficulty == '2':
		word = random.choice(word6)
		guesses_left = 7
	else:	
		word = random.choice(word7)
		guesses_left = 6
	return word, guesses_left


def validate_display(word, guesses_left):
	guess = 'X'
	while guess=='X':
		guess = input('What word do you want to guess? ')
		if len(guess) != len(word):
			print("You're guess is not the right length! Please guess again.")
			guess = 'X'
		else:
			for char in guess:
				if not char.isalpha():
					print("This is not a word, it has one or more special characters. Please guess again.")
					guess = 'X'
					break
		
		if guess != 'X':		
			output = ''
			guess = guess.lower()
			for i in range(len(guess)):
				if guess[i]==word[i]:
					output+=(f'\033[92m{(guess[i])}')
				elif guess[i] in word:
					output += (f'\033[93m{guess[i]}')
				else:
					output += (f'\033[91m{guess[i]}')
			print(output)
			if win_loss(guess, word, guesses_left):
				break
			guesses_left-=1
		

def win_loss(guess, word, guesses_left):
	if guess==word:
		print(f'You guessed correct!!! The word was {word}.\033[0m')
		return True
	else:
		if guesses_left>1:
			guesses_left-=1
			print(f'\033[0mYou have {guesses_left} guesses left.')
			return False

		else:
			print(f'\033[0mYou ran out of guesses :( \nThe word was {word}.')
			return True

main()
