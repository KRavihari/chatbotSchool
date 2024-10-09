import re
import responsesChatbot1 as long

def message_Probability(useer_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_word=True
    
    #Counts how many words are present in each predefined message
    for word in useer_message:
        if word in recognised_words:
            message_certainty+=1

    #Calculate the percent of recognised words in a user message
    percentage=float(message_certainty)/float(len(recognised_words))     

    for word in required_words:
        if word not in useer_message:
            has_required_word=False
            break

    if has_required_word or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_Probability(message,list_of_words,single_response,required_words)

    #Response ....................................
        
    response('Hello!',['hello','hi','hai','hey','hlo','hola'],single_response=True)
    response('I\'m doing fine, and you?',['how','are','you','doing'],required_words=['how','doing'])
    response('Thank you!',['love','code','coding','you'])
    #response(long.R_EATING,['what','eat','eating','eaten'])
    response("Choose subjects based on your interests, strengths, and future career goals. Think about what subjects you enjoy and excel in. Research how these subjects align with potential careers you're interested in, such as medicine, engineering, or the arts",['choose','a\l','al','A/L','subjects','how','AL'])
    response("To apply for medical school, you need to study Biology, Chemistry, and Physics or Agriculture for your A/Ls. You should also have a strong academic record in science-related subjects.",['what','a/l','A/L','subjects','required','medical school','for','enter'])
    response("Yes, but it depends on how far you are into the program. Changing subjects early in your A/Ls is easier, but it could be more challenging later as you'll need to catch up on the new material.",['can','change','A/L','subject','subjects','after','starting'])
    response('The main A/L streams are Science (Biology, Physics, Chemistry), Commerce (Accounting, Business Studies, Economics), and Arts (Languages, History, Political Science).',['what','are','main','A/L','subject','streams','Sri Lanka'])
    response("If you're interested in engineering, choose the Physical Science stream with subjects like Physics, Combined Mathematics, and Chemistry.",['which','A/L','stream','should','choose','career','in','engineering'])
    response('The University of Colombo, University of Peradeniya, University of Kelaniya, and University of Sri Jayewardenepura are well-known for their science faculties.',['best','universities','what','science','students'])
    response('Commerce stream opens up careers in accounting, finance, marketing, business management, banking, and economics. You can also pursue professional qualifications like CIMA or ACCA.',['career','options','commerce','stream','what'])
    response(" Visit the University Grants Commission (UGC) website for the latest admission requirements and Z-score cut-offs for various degree programs.",['university','admission','requirements','find','how','where'])
    response('Depending on your stream, you can start qualifications like CIMA, ACCA (Commerce), or foundation courses in IT or engineering. Always ensure it doesn’t affect your A/L preparation.',['professional','qualifications','alongside','along with','at the same time'])
    response('Critical soft skills include communication, teamwork, time management, problem-solving, and adaptability. Developing these skills alongside academics is essential for career success.',['important','soft skills','future'])
    response('Join your school’s debate team, participate in speech competitions, or practice by presenting in front of small groups. Online platforms like TED-Ed and Toastmasters also provide guidance.',['how','improve','public','speaking','skills'])
    response('You can study computer science, information technology, software engineering, or data science. Look into universities like the University of Colombo and the Sri Lanka Institute of Information Technology (SLIIT).',['courses','IT','field'])
    response('Careers in arts and humanities include teaching, journalism, law, psychology, history, political science, and languages. You can also explore creative industries like writing and design.',['career paths','courses','arts','humanities'])
    response('Practice past papers, focus on weak areas, and create a study timetable. Consider joining revision classes or online tutorials to help you stay on track.',['prepare','university','entrance','exams','exam','how'])
    response('Biology A/Ls can lead to careers in medicine, biotechnology, environmental science, nursing, and medical research. You could also pursue degrees in agriculture or veterinary science.',['A/L','biology','bio stream','choose','study','select','jobs','opportunities','what'])
    response('Yes, many universities in Sri Lanka offer scholarships based on academic merit, sports achievements, and financial need. Check each university’s scholarship programs for details.',['available','scholarships'])
    response("Focus on problem-solving, critical thinking, technical knowledge (math and physics), and communication. It’s also beneficial to work on software skills like coding and using engineering tools.",['skills','develop','career','engineering','in'])
    response('Yes, you can pursue a career in IT by taking IT-related foundation courses or diplomas after your A/Ls, even if you study Arts. Many universities offer flexible paths to enter IT fields.',['learn','study','IT','even','arts','A/L'])
    response('Review your A/L results, check the Z-score cut-off for various degrees, and consider your interests and career aspirations. Consult the UGC guide or university websites to explore options.',['choose','A/L','result','results','select','university','program','based','on'])
    response('Don’t panic. You can reattempt your A/Ls, explore vocational training, or pursue alternative higher education options like private universities or professional courses.',['hoped',"didn't",'get','desired','A/L','results','what','to','do'])
    response('If you choose not to attend university, you can explore vocational training, pursue professional certifications (like ACCA, CIMA, or IT diplomas), or start working in fields like hospitality, retail, or technology.',['options','do not','want',"don't",'what','are','go','to','university','after','A/L'])
    response('Vocational training institutes like the National Apprentice and Industrial Training Authority (NAITA) and the Tertiary and Vocational Education Commission (TVEC) offer courses in areas like automotive engineering, carpentry, beauty, ICT, and more.',['vocational','training','options','available'])
    response('The tourism industry offers careers in hospitality management, travel agencies, hotel administration, tour guiding, and event planning. Specialized courses are available through institutions like the Sri Lanka Institute of Tourism and Hotel Management (SLITHM).',['career','opportunities','tourism industry','tourism'])
    response('Consider your career goals, learning preferences, and financial situation. University provides theoretical knowledge and broad career options, while vocational training is more hands-on and can lead to quicker job placements in specific trades.',['between','vocational training','decide'])
    response('The University of Colombo, University of Sri Jayewardenepura, and the University of Kelaniya are well-regarded for business and management programs. You can also explore private universities like NSBM Green University and SLIIT.',['best','universities','business','and','&','management','studies','what'])
    response('With a degree in psychology, you can become a clinical psychologist, counseling psychologist, educational psychologist, or work in research, human resources, or social services. Institutions like the University of Colombo and private universities offer psychology programs.',['career','options','available','field of psychology','psychology','opportunities'])
    response('Focus on your A/L studies and aim for high grades. Participate in extracurricular activities, demonstrate leadership, and show a commitment to community service. Strong recommendation letters and a well-rounded application can also make a difference.',['improve','chances','able to','getting','into','top','university','best'])
    response('In-demand fields include IT and software development, healthcare (doctors, nurses, medical technicians), engineering, business management, and finance. These industries are growing and offer good job prospects.',['study','high','demand','fields'])
    response('Some schools and private organizations offer scholarships based on academic performance in science subjects. For higher education, check university-specific scholarships like the Mahapola and Bursary schemes for A/L students who perform well in science.',['scholarships','available','school students','students','pursing','A/L','in','science'])
    response('Look for internships, part-time jobs, or volunteer opportunities related to your field of interest. Many companies, especially in IT and business sectors, offer internships to A/L students or recent graduates.',['gain','while','studying','learning','work','experience','work experience'])
    response('Mathematics can lead to careers in fields like data science, actuarial science, finance, engineering, teaching, and research. You can also pursue specialized degrees in statistics, analytics, or economics.',['careers','related','maths','mathematics','major','background','in'])
    response('With a degree in agriculture, you can work in agribusiness management, research and development, environmental science, horticulture, or food technology. The University of Peradeniya and University of Ruhuna offer strong programs in agriculture.',['career','opportunities','agriculture'])
    response('The Open University of Sri Lanka (OUSL) offers a wide range of distance learning programs in fields like engineering, management, social sciences, and health sciences. Other private institutions also offer online degree options.',['which','universities','offer','distance','learning','programs'])
    response('To become a software developer, study IT or computer science at a recognized university. You can also learn through online courses, bootcamps, and certifications in programming languages like Java, Python, and web development.',['sofware developer','become','how'])
    response('Careers in environmental science include working as an environmental consultant, conservationist, ecologist, or sustainability expert. You could also work in waste management, wildlife protection, or green energy sectors.',['careers','what','pursue','select','environmental science'])
    response('Law graduates can become lawyers, judges, or legal advisors. You can also work in corporate law, human rights, or international law. To pursue a law career, you need to pass the Law College entrance exam and complete legal studies at the Sri Lanka Law College.',['career','opportunities','law'])
    response('To become a chartered accountant, you can start by joining the Institute of Chartered Accountants of Sri Lanka (CA Sri Lanka) and complete their professional qualification while gaining work experience in the field of accounting or finance.',['process','of','becoming','chartered','accountant','become','a'])
    response("If you're skilled in languages, consider careers in teaching, translation, journalism, international relations, or tourism. You can also pursue higher studies in linguistics, communication, or become a language specialist for international organizations.",['career','options','opportuities','not','good','at','languages','bad','in'])
    response('Take online courses or join local IT classes to improve your computer skills. Learn to use essential software like Microsoft Office, internet research tools, and coding languages like Python or HTML for more advanced digital literacy',['improve','digital','literacy','skills','how'])
    response("Extracurricular activities play an important role in university applications, especially if you're applying for leadership or scholarship programs. Involvement in sports, clubs, volunteer work, and competitions shows a well-rounded personality and leadership skills.",['how','important','extracurricular','activities','involvement','involving','in','university application','applying','university'])
        

    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match]< 1  else best_match                  

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response
while True:
    print('Mia: ' + get_response(input('You: ')))