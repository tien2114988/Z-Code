import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_100(self):
        self.assertTrue(TestLexer.test("abdhd##abc\nabcd,123.39","abdhd,\n,abcd,,,123.39,<EOF>",100))
    
    def test_101(self):
        self.assertTrue(TestLexer.test("##abc","<EOF>",101))

    def test_102(self):
        self.assertTrue(TestLexer.test("####shcccc","<EOF>",102))
        
    def test_103(self):
        self.assertTrue(TestLexer.test("#abc","Error Token #",103))

    def test_104(self):
        self.assertTrue(TestLexer.test("####shcccc\n c","\n,c,<EOF>",104))
        
    def test_105(self):
        self.assertTrue(TestLexer.test("abc12","abc12,<EOF>",105))
        
    def test_106(self):
        self.assertTrue(TestLexer.test("_abcABc23","_abcABc23,<EOF>",106))
        
    def test_107(self):
        self.assertTrue(TestLexer.test("4A_abc","4,A_abc,<EOF>",107))
        
    def test_108(self):
        self.assertTrue(TestLexer.test("A12_abc","A12_abc,<EOF>",108))
        
    def test_109(self):
        self.assertTrue(TestLexer.test("abc 4hd","abc,4,hd,<EOF>",109))
        
    def test_110(self):
        self.assertTrue(TestLexer.test("abc Abc _ABC_","abc,Abc,_ABC_,<EOF>",110))
        
    def test_111(self):
        self.assertTrue(TestLexer.test("abc Abc _ABC_","abc,Abc,_ABC_,<EOF>",111))
        
    def test_112(self):
        self.assertTrue(TestLexer.test("true","true,<EOF>",112))
        
    def test_113(self):
        self.assertTrue(TestLexer.test("false","false,<EOF>",113))
        
    def test_114(self):
        self.assertTrue(TestLexer.test("number","number,<EOF>",114))
        
    def test_115(self):
        self.assertTrue(TestLexer.test("func","func,<EOF>",115))
        
    def test_116(self):
        self.assertTrue(TestLexer.test("func##func","func,<EOF>",116))
        
    def test_117(self):
        self.assertTrue(TestLexer.test("abc + cde ... hfg","abc,+,cde,...,hfg,<EOF>",117))
        
    def test_118(self):
        self.assertTrue(TestLexer.test("abc and cde or hfg","abc,and,cde,or,hfg,<EOF>",118))
        
    def test_119(self):
        self.assertTrue(TestLexer.test("abc <= cde % hg","abc,<=,cde,%,hg,<EOF>",119))
        
    def test_120(self):
        self.assertTrue(TestLexer.test("(abc)[cde]\n","(,abc,),[,cde,],\n,<EOF>",120))
      
    ##   
    def test_121(self):
        self.assertTrue(TestLexer.test("##abc \n abc","\n,abc,<EOF>",121))
        
    def test_122(self):
        self.assertTrue(TestLexer.test("233","233,<EOF>",122))  
        
    def test_123(self):
        self.assertTrue(TestLexer.test("00233.345","00233.345,<EOF>",123)) 
        
    def test_124(self):
        self.assertTrue(TestLexer.test("233.345","233.345,<EOF>",124)) 
        
    def test_125(self):
        self.assertTrue(TestLexer.test("233.","233.,<EOF>",125))         
        
    def test_126(self):
        self.assertTrue(TestLexer.test(".123","Error Token .",126))         
        
    def test_127(self):
        self.assertTrue(TestLexer.test("233e1","233e1,<EOF>",127))  
        
    def test_128(self):
        self.assertTrue(TestLexer.test("23e-3","23e-3,<EOF>",128))
        
    def test_129(self):
        self.assertTrue(TestLexer.test("23e+3","23e+3,<EOF>",129))  
        
    def test_130(self):
        self.assertTrue(TestLexer.test("23E+31","23E+31,<EOF>",130))  
        
    def test_131(self):
        self.assertTrue(TestLexer.test("e+31","e,+,31,<EOF>",131))  
        
    def test_132(self):
        self.assertTrue(TestLexer.test("e31","e31,<EOF>",132))  
        
    def test_133(self):
        self.assertTrue(TestLexer.test("233.3e1","233.3e1,<EOF>",133))  
        
    def test_134(self):
        self.assertTrue(TestLexer.test("23.3e-3","23.3e-3,<EOF>",134))
        
    def test_135(self):
        self.assertTrue(TestLexer.test("23.3e+3","23.3e+3,<EOF>",135))  
        
    def test_136(self):
        self.assertTrue(TestLexer.test("23.3e+31","23.3e+31,<EOF>",136))  
        
    def test_137(self):
        self.assertTrue(TestLexer.test("23.E+31","23.E+31,<EOF>",137))
        
    def test_138(self):
        self.assertTrue(TestLexer.test("23.e","23.,e,<EOF>",138))
        
    def test_139(self):
        self.assertTrue(TestLexer.test("truefalse","truefalse,<EOF>",139))
        
    def test_140(self):
        self.assertTrue(TestLexer.test("true##abc \n true","true,\n,true,<EOF>",140))

    def test_141(self):
        self.assertTrue(TestLexer.test(""" "abc" ""","abc,<EOF>",141))
        
    def test_142(self):
        self.assertTrue(TestLexer.test(""" "abc\tabc" ""","""abc\tabc,<EOF>""",142))
        
    def test_143(self):
        self.assertTrue(TestLexer.test(""" "abc\b\fc" ""","abc\b\fc,<EOF>",143))
        
    def test_144(self):
        self.assertTrue(TestLexer.test(""" "def\\b\'c" ""","""def\\b\'c,<EOF>""",144))
    
    def test_145(self):
        self.assertTrue(TestLexer.test(""" ""","<EOF>",145))
        
    def test_146(self):
        self.assertTrue(TestLexer.test(""" "abc'd"  ""","""abc'd,<EOF>""",146))
        
    def test_147(self):
        self.assertTrue(TestLexer.test(""" "abca\\rbc" ""","""abca\\rbc,<EOF>""",147))
    
    #   
    def test_148(self):
        self.assertTrue(TestLexer.test(""" "def'" ""","""Unclosed String: def'" """,148))
        
    def test_149(self):
        self.assertTrue(TestLexer.test(""" " ""","""Unclosed String:  """,149))
        
    def test_150(self):
        self.assertTrue(TestLexer.test(""" "'" ""","""Unclosed String: '" """,150))
        
    def test_151(self):
        self.assertTrue(TestLexer.test(""" "abc'"abnc'"" ""","""abc'"abnc'",<EOF>""",151))
        
    def test_152(self):
        self.assertTrue(TestLexer.test(""" "abc\kahd" ""","""Illegal Escape In String: abc\k""",152))
        
    def test_153(self):
        self.assertTrue(TestLexer.test(""" "abc\h aj'" ""","""Illegal Escape In String: abc\h""",153))
        
    def test_154(self):
        self.assertTrue(TestLexer.test(""" "abc\ aj'" ""","""Illegal Escape In String: abc\ """,154))
        
    def test_155(self):
        self.assertTrue(TestLexer.test(""" "\i" ""","""Illegal Escape In String: \i""",155))
        
    def test_156(self):
        self.assertTrue(TestLexer.test(""" ??? ""","""Error Token ?""",156))
        
    def test_157(self):
        self.assertTrue(TestLexer.test(""" abc,[?] ""","""abc,,,[,Error Token ?""",157))
        
    def test_158(self):
        self.assertTrue(TestLexer.test("""\n\n\n\n""","""\n,\n,\n,\n,<EOF>""",158))
        
    def test_159(self):
        self.assertTrue(TestLexer.test("""##\n\n\n\n""","""\n,\n,\n,\n,<EOF>""",159))
        
    def test_160(self):
        self.assertTrue(TestLexer.test("""abcdef##\nkgh""","""abcdef,\n,kgh,<EOF>""",160))
        
    def test_161(self):
        self.assertTrue(TestLexer.test(""" "Hello this is a '"test'")""","""Unclosed String: Hello this is a '"test'")""",161))
        
    def test_162(self):
        self.assertTrue(TestLexer.test(""" "Hello\nabc""","""Unclosed String: Hello""",162))
        
    def test_163(self):
        self.assertTrue(TestLexer.test("""true false number bool string return var dynamic func for until by break continue if else elif begin end not and or""","""true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>""",163))
        
    def test_164(self):
        self.assertTrue(TestLexer.test("""+ - * / % not and or = <- != < <= > >= ... ==""","""+,-,*,/,%,not,and,or,=,<-,!=,<,<=,>,>=,...,==,<EOF>""",164))
        
    def test_165(self):
        self.assertTrue(TestLexer.test("""( ) [ ] , \n""","""(,),[,],,,\n,<EOF>""",165))
        
    def test_166(self):
        self.assertTrue(TestLexer.test("""(a+true-false) [00e-3 + 00.22E+2] if(a+b) begin for until""","""(,a,+,true,-,false,),[,00e-3,+,00.22E+2,],if,(,a,+,b,),begin,for,until,<EOF>""",166))
        
    def test_167(self):
        self.assertTrue(TestLexer.test("""func voi(number a, string b) begin
        var i <- 0
        for i until i >= 10 by 1
        writeNumbe(i)
        end""","""func,voi,(,number,a,,,string,b,),begin,\n,var,i,<-,0,\n,for,i,until,i,>=,10,by,1,\n,writeNumbe,(,i,),\n,end,<EOF>""",167))
    
    def test_168(self):
        self.assertTrue(TestLexer.test("""number abc["rtien"] <- [[1,2,y],[2,"asd",true,x]] 
        ""","""number,abc,[,rtien,],<-,[,[,1,,,2,,,y,],,,[,2,,,asd,,,true,,,x,],],\n,<EOF>""",168))
        
    def test_169(self):
        self.assertTrue(TestLexer.test("""func foo() begin
        
        abc(1,2,3)
        return a+b+c-a*abc(1,2,a) % a[1,2,3]
        end
        
        ""","""func,foo,(,),begin,\n,\n,abc,(,1,,,2,,,3,),\n,return,a,+,b,+,c,-,a,*,abc,(,1,,,2,,,a,),%,a,[,1,,,2,,,3,],\n,end,\n,\n,<EOF>""",169))
        
    def test_170(self):
        self.assertTrue(TestLexer.test("""func foo(number a, string b, bool b[1,2,3])
        begin
            if (a+b) a <- b + 1 
            elif (a+c) a[1,2] <- 4
        end
        ""","""func,foo,(,number,a,,,string,b,,,bool,b,[,1,,,2,,,3,],),\n,begin,\n,if,(,a,+,b,),a,<-,b,+,1,\n,elif,(,a,+,c,),a,[,1,,,2,],<-,4,\n,end,\n,<EOF>""",170))
        
    def test_171(self):
        self.assertTrue(TestLexer.test("""func main() begin
        string s <- writeString("Hello this is a '"test'")
        end
        ""","""func,main,(,),begin,\n,string,s,<-,writeString,(,Unclosed String: Hello this is a '"test'")""",171))
        
    def test_172(self):
        self.assertTrue(TestLexer.test("""number a
        string _abc23 <- "ngyen dai tin"
        
        bool  Ad_2k3c <- false""","""number,a,\n,string,_abc23,<-,ngyen dai tin,\n,\n,bool,Ad_2k3c,<-,false,<EOF>""",172))
        
    def test_173(self):
        self.assertTrue(TestLexer.test("""var AHDHD <- true
        
         
        dynamic k34533 <- 12.002E+234
        
        number A_adh0239[2,3,4,2] <- ["nguyen dai tien", 1, [1,2,3], abc(abc, _cde), _cde()]
        
        
        string __abcd[1]""","""var,AHDHD,<-,true,\n,\n,\n,dynamic,k34533,<-,12.002E+234,\n,\n,number,A_adh0239,[,2,,,3,,,4,,,2,],<-,[,nguyen dai tien,,,1,,,[,1,,,2,,,3,],,,abc,(,abc,,,_cde,),,,_cde,(,),],\n,\n,\n,string,__abcd,[,1,],<EOF>""",173))
        
    def test_174(self):
        self.assertTrue(TestLexer.test("""bool a[1,2,3] <- a/ not 2 * (3 == b % 4) ... (b == (c != d and 3 + 4 + 5 or 234) ... -abc(abc(), "nguyenditien")[cde(),"nguyen dait ein", true, false] )
        
        func _adhi24()
        func _afhi34(number abc, string cad, bool dhsj)""","""bool,a,[,1,,,2,,,3,],<-,a,/,not,2,*,(,3,==,b,%,4,),...,(,b,==,(,c,!=,d,and,3,+,4,+,5,or,234,),...,-,abc,(,abc,(,),,,nguyenditien,),[,cde,(,),,,nguyen dait ein,,,true,,,false,],),\n,\n,func,_adhi24,(,),\n,func,_afhi34,(,number,abc,,,string,cad,,,bool,dhsj,),<EOF>""",174))
        
    def test_175(self):
        self.assertTrue(TestLexer.test("""4E-2 - 4E - 2""","""4E-2,-,4,E,-,2,<EOF>""",175))
        
    def test_176(self):
        self.assertTrue(TestLexer.test("""if ((abc+e-2)) 
            begin
                if(true) return ## aefiefei
            end""","""if,(,(,abc,+,e,-,2,),),\n,begin,\n,if,(,true,),return,\n,end,<EOF>""",176))
        
    def test_177(self):
        self.assertTrue(TestLexer.test("""\\b\n""","""Error Token \\""",177))
        
    def test_178(self):
        self.assertTrue(TestLexer.test("""#######abcdch\n#######uscguscgu\n#####ii\nsfe""","""\n,\n,\n,sfe,<EOF>""",178))
        
    def test_179(self):
        self.assertTrue(TestLexer.test("""number A_adh0239[2,3,4,2] <- ["nguyen dai tien", 1, [1,2,3], abc(abc, _cde), _cde()]
            
            if ((abc+e-2)) 
            begin
                if(true) return ## aefiefei
            end""","""number,A_adh0239,[,2,,,3,,,4,,,2,],<-,[,nguyen dai tien,,,1,,,[,1,,,2,,,3,],,,abc,(,abc,,,_cde,),,,_cde,(,),],\n,\n,if,(,(,abc,+,e,-,2,),),\n,begin,\n,if,(,true,),return,\n,end,<EOF>""",179))
                
    def test_180(self):
        self.assertTrue(TestLexer.test("""ngd(a["tien",12,bcd()],23,true,false,"tieh\i)
            end
            ## diatie ""","""ngd,(,a,[,tien,,,12,,,bcd,(,),],,,23,,,true,,,false,,,Illegal Escape In String: tieh\i""",180))
        
    def test_181(self):
        self.assertTrue(TestLexer.test("""false,"tieh'"ac")""","""false,,,tieh'"ac,),<EOF>""",181))
        
    def test_182(self):
        self.assertTrue(TestLexer.test(""" "abc'"acfhi""","""Unclosed String: abc'"acfhi""",182))
            
    def test_183(self):
        self.assertTrue(TestLexer.test("""number <- anc + 2""","""number,<-,anc,+,2,<EOF>""",183))
        
    def test_184(self):
        self.assertTrue(TestLexer.test("""string,number == - + 2""","""string,,,number,==,-,+,2,<EOF>""",184))
        
    def test_185(self):
        self.assertTrue(TestLexer.test("""bool== - - 2""","""bool,==,-,-,2,<EOF>""",185))
        
    def test_186(self):
        self.assertTrue(TestLexer.test("""abcdh number until""","""abcdh,number,until,<EOF>""",186))
        
    def test_187(self):
        self.assertTrue(TestLexer.test("""==,-,2""","""==,,,-,,,2,<EOF>""",187))
        
            
    def test_188(self):
        self.assertTrue(TestLexer.test(""" "'" """, """Unclosed String: '" """,188))
            
            
    def test_189(self):
        self.assertTrue(TestLexer.test("\"'\"", """',<EOF>""",189))
        
    def test_190(self):
        self.assertTrue(TestLexer.test("""##"abc\nefght ""","""\n,efght,<EOF>""",190))
        
    def test_191(self):
        self.assertTrue(TestLexer.test(""" "abc\" ""","""abc,<EOF>""",191))
        
    def test_192(self):
        self.assertTrue(TestLexer.test(""" "abc\\" ""","""Illegal Escape In String: abc\\\"""",192))
        
    def test_193(self):
        self.assertTrue(TestLexer.test(""" "abc\\i" ""","""Illegal Escape In String: abc\i""",193))
        
    def test_194(self):
        self.assertTrue(TestLexer.test(""" "abc\k" ""","""Illegal Escape In String: abc\k""",194))
        
    def test_195(self):
        self.assertTrue(TestLexer.test(""" "abc\'" ""","""Unclosed String: abc'" """,195))
        
    def test_196(self):
        self.assertTrue(TestLexer.test(""" "abc'" ""","""Unclosed String: abc'" """,196))
        
    ##
    def test_197(self):
        self.assertTrue(TestLexer.test(""" "abca\nbc" ""","""abca\n\nbc,<EOF>""",197))
    
    ## 
    def test_198(self):
        self.assertTrue(TestLexer.test(""" "abca\bc" ""","""abca\bc,<EOF>""",198))
        
    def test_199(self):
        self.assertTrue(TestLexer.test(""" "abca\\ rbc\" ""","""Illegal Escape In String: abca\\ """,199))
        
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def test_149(self):
    #     self.assertTrue(TestLexer.test(' "abca"rbc" ',"""abca,rbc,Unclosed String:  """,149))
        
    # def test_150(self):
    #     self.assertTrue(TestLexer.test(""" "abcadf""","""Unclosed String: abcadf""",150))
        
    # def test_151(self):
    #     self.assertTrue(TestLexer.test(""" "ab\idf" ""","""Illegal Escape In String: ab\i""",151))
        
    # #
    # def test_152(self):
    #     self.assertTrue(TestLexer.test(""" "'" ""","""Unclosed String: '" """,152))
        
    # def test_153(self):
    #     self.assertTrue(TestLexer.test(""" "nguyen dai tien \k abc ""","""Illegal Escape In String: nguyen dai tien \k""",153))
        
    # def test_154(self):
    #     self.assertTrue(TestLexer.test(""" "nguyen dai \b \k abc ""","""Illegal Escape In String: nguyen dai \b \k""",154))
        
    # def test_155(self):
    #     self.assertTrue(TestLexer.test(""" "nguyen dai \t \" ""","""Illegal Escape In String: nguyen dai \t \"""",155))
        
    # def test_156(self):
    #     self.assertTrue(TestLexer.test(""" "nguyen dai \\""","""Unclosed String: nguyen dai \\""",154))
        
  