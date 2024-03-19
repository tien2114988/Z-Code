import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        """Simple program: int main() {} """
        input = """number true
        """
        expect = "Error on line 1 col 7: true"
        self.assertTrue(TestParser.test(input,expect,200))
    
    def test_201(self):
        """Simple program: int main() {} """
        input = """number a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_202(self):
        """Simple program: int main() {} """
        input = """string a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_203(self):
        """Simple program: int main() {} """
        input = """bool a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        
    def test_204(self):
        """Simple program: int main() {} """
        input = """var a
        """
        expect = "Error on line 1 col 6: \n"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_205(self):
        """Simple program: int main() {} """
        input = """dynamic a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    
    def test_206(self):
        """Simple program: int main() {} """
        input = """var b <- 3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_207(self):
        """Simple program: int main() {} """
        input = """number b <- 57
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_208(self):
        """Simple program: int main() {} """
        input = """number b <- 58"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_209(self):
        """Simple program: int main() {} """
        input = """var b <- true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_210(self):
        """Simple program: int main() {} """
        input = """string b <- 15
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        
    def test_211(self):
        """Simple program: int main() {} """
        input = """string b <- 20 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_212(self):
        """Simple program: int main() {} """
        input = """dynamic b <- 25
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
        
    def test_213(self):
        """Simple program: int main() {} """
        input = """bool b <- true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
        
    def test_214(self):
        """Simple program: int main() {} """
        input = """bool b <- 16 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_215(self):
        """Simple program: int main() {} """
        input = """number a[1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_216(self):
        """Simple program: int main() {} """
        input = """string a[1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_217(self):
        """Simple program: int main() {} """
        input = """bool a[1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        
    def test_218(self):
        """Simple program: int main() {} """
        input = """var a[1,2,3]
        """
        expect = "Error on line 1 col 5: ["
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_219(self):
        """Simple program: int main() {} """
        input = """dynamic a[1,2,3]
        """
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_220(self):
        """Simple program: int main() {} """
        input = """number a <- a+b+1+2-3*5%6/4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
        
    def test_221(self):
        """Simple program: int main() {} """
        input = """number a <- "dai tien" ... "tien" and a or b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
        
    def test_222(self):
        """Simple program: int main() {} """
        input = """bool a <- not a + - a == 123.e-123
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        
    def test_223(self):
        """Simple program: int main() {} """
        input = """bool a <- num1 % num2 = 0 or num2 % num1 = 0
        """
        expect = "Error on line 1 col 41: ="
        self.assertTrue(TestParser.test(input,expect,223))
        
    def test_224(self):
        """Simple program: int main() {} """
        input = """dynamic a <- (num1 % num2 = 0) or (num2 % num1 = 0)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        
    def test_225(self):
        """Simple program: int main() {} """
        input = """var a <- 2 (-2)
        """
        expect = "Error on line 1 col 11: ("
        self.assertTrue(TestParser.test(input,expect,225))
        
    def test_226(self):
        """Simple program: int main() {} """
        input = """a <- 2
        """
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input,expect,226))
        
    def test_227(self):
        """Simple program: int main() {} """
        input = """number a <- a[b[2, 3]] + 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
        
    def test_228(self):
        """Simple program: int main() {} """
        input = """number a <- [1,["tine",2,true],4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
        
    def test_229(self):
        """Simple program: int main() {} """
        input = """number a <- []
        """
        expect = "Error on line 1 col 13: ]"
        self.assertTrue(TestParser.test(input,expect,229))
        
    def test_230(self):
        """Simple program: int main() {} """
        input = """number a <- [1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
        
    def test_231(self):
        """Simple program: int main() {} """
        input = """number a[1] <- [1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
        
    def test_232(self):
        """Simple program: int main() {} """
        input = """number a[1,"tien"] <- [1]
        """
        expect = "Error on line 1 col 11: tien"
        self.assertTrue(TestParser.test(input,expect,232))
        
    def test_233(self):
        """Simple program: int main() {} """
        input = """number a[1,2] <- [1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        
    def test_234(self):
        """Simple program: int main() {} """
        input = """number a[] <- [1]
        """
        expect = "Error on line 1 col 9: ]"
        self.assertTrue(TestParser.test(input,expect,234))
        
    def test_235(self):
        """Simple program: int main() {} """
        input = """number a <- a[1][2]
        """
        expect = "Error on line 1 col 16: ["
        self.assertTrue(TestParser.test(input,expect,235))
        
    def test_236(self):
        """Simple program: int main() {} """
        input = """number a <- a[b[c["toan",2],true],"tien"] 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        
    def test_237(self):
        """Simple program: int main() {} """
        input = """number a <- a + tien()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        
    def test_238(self):
        """Simple program: int main() {} """
        input = """number a <- tieng(1+2,abc(123),"kk",a,true,a[1,2]) + tien()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_239(self):
        """Simple program: int main() {} """
        input = """number a <- tieng(1+2,abc(123),"kk",a,true,a[1,2]) + tien(a[a[b[c["toan",2],true],"tien"]])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
        
    def test_240(self):
        """Simple program: int main() {} """
        input = """number a <- b##tien
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
        
    def test_241(self):
        """Simple program: int main() {} """
        input = """number a <- b
        ##tien
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        
    def test_242(self):
        """Simple program: int main() {} """
        input = """number a <- 3[1]
        """
        expect = "Error on line 1 col 13: ["
        self.assertTrue(TestParser.test(input,expect,242))
        
    def test_243(self):
        """Simple program: int main() {} """
        input = """number a <-  not a and -2 <= 4 or 6 ... a[1,2,3] + a[b(2,3)] - a[b(2,3),"tien"] != a[b(2,3)] * abc(3) / false % true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
        
    def test_244(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        begin
        number a <- a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
        
    def test_245(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        begin
        number a <- a
        end"""
        expect = "Error on line 4 col 11: <EOF>"
        self.assertTrue(TestParser.test(input,expect,245))
        
    def test_246(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)begin
        
        
        number a <- a
        
        
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
        
    def test_247(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        
        begin
        number a 
        a <- not a and -2 <= 4 or 6 ... a[1,2,3] + a[b(2,3)] - a[b(2,3),"tien"] != a[b(2,3)] * abc(3) / false % true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_247(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        
        begin
        number a a <- not a and -2 <= 4 or 6 ... a[1,2,3] + a[b(2,3)] - a[b(2,3),"tien"] != a[b(2,3)] * abc(3) / false % true
        end
        """
        expect = "Error on line 4 col 17: a"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_248(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        number a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
        
    def test_249(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        
    def test_250(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)begin
        begin
        number a [1,2,3]
        abc()[1+2,abc(),[1,2,3]] <- [[1,23],"tien"]
        end
        end
        """
        expect = "Error on line 4 col 13: ["
        self.assertTrue(TestParser.test(input,expect,250))
        
    def test_251(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)begin
        begin
        number a [1,2,3]
        ab[1+2,abc(),[1,2,3]] <- [[1,23],"tien"]
        end
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,251))
        
    def test_252(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)begin
        begin
        number a [1,2,3]
        return abc()[1+2,abc(),[1,2,3]] <- [[1,23],"tien"]
        end
        """
        expect = "Error on line 4 col 40: <-"
        self.assertTrue(TestParser.test(input,expect,252))
        
    def test_253(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        begin
            if (a+b) a <- b + 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        
    def test_254(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b[1,2,3])
        begin
            if (a+b) a <- b + 1 elif (a+c) a[1,2] <- 4
        end
        """
        expect = "Error on line 3 col 32: elif"
        self.assertTrue(TestParser.test(input,expect,254))
        
    def test_255(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b)
        begin
            if (a+b) a <- b + 1 
            elif (a+c) a[1,2] <- 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
        
    def test_256(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b[1,2,3])
        begin
            if (a+b) a <- b + 1 
            elif (a+c) a[1,2] <- 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
        
    def test_256(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b[1,2+3,3])
        begin
            if (a+b) a <- b + 1 
            elif (a+c) a[1,2] <- 4
        end
        """
        expect = "Error on line 1 col 39: +"
        self.assertTrue(TestParser.test(input,expect,256))
        
    def test_257(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b[1,3,3])
        begin
            if (a+b) a <- b + 1 
            
            elif (a+c) 
            
            a[1,2] <- 4
            
            elif (a==b) 
            abc()
            
            
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        
    def test_258(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b[1,3,3])
        begin
            if (a+b) a <- b + 1 
            
            elif (a+c) 
            
            a[1,2] <- 4
            
            elif (a==b) 
            abc()
            else 
            
        end
        """
        expect = "Error on line 13 col 8: end"
        self.assertTrue(TestParser.test(input,expect,258))
        
    def test_259(self):
        """Simple program: int main() {} """
        input = """func foo(number a, string b, bool b[1,3,3])
        begin
            if (a+b) a <- b + 1 
            
            elif (a+c) 
            
            a[1,2] <- 4
            
            elif (a==b) 
            abc()
            else
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
        
    def test_260(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            elif (a+c) 
            
            a[1,2] <- 4
            
            elif (a==b) 
            abc()
            else 
            
            abc()[1,2] <- true + false
        end
        
        
        """
        expect = "Error on line 3 col 12: elif"
        self.assertTrue(TestParser.test(input,expect,260))
        
    def test_261(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            if (a+c) 
            begin
            a[1,2] <- 4
            end
            elif (a==b) 
            abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
        
    def test_262(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            if (a+c) 
            begin
            a[1,2] <- 4
            end elif (a==b) 
            abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "Error on line 6 col 16: elif"
        self.assertTrue(TestParser.test(input,expect,262))
        
    def test_263(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
            number a
            a <- a+b
            end 
            if (a+c) 
            begin
            a[1,2] <- 4
            end 
            elif (a==b) 
            abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        
    def test_264(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
            number a
            a <- a+b
            end if (a+c) 
            begin
            a[1,2] <- 4
            end 
            elif (a==b) 
            abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "Error on line 6 col 16: if"
        self.assertTrue(TestParser.test(input,expect,264))
        
    def test_265(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 a <- 234
            end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
        
    def test_266(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh 
                by 1233 
                a <- 234
            end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "Error on line 4 col 45: \n"
        self.assertTrue(TestParser.test(input,expect,266))
        
    def test_267(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 
                
                
                
                a <- 234
            end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
        
    def test_268(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 
                
                
                
                a <- 234 end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "Error on line 8 col 25: end"
        self.assertTrue(TestParser.test(input,expect,268))
        
    def test_269(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin for abcd until abcd >= efgh by 1233 
                
                
                
                a <- 234 
            end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "Error on line 3 col 18: for"
        self.assertTrue(TestParser.test(input,expect,269))
        
    def test_270(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 
                
                
                
                a <- 234 
            end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
        
    def test_271(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 
                begin 
                
                
                break
                
                end
                
                
                a <- 234 
            end 
            
            if (a+c) 
                begin
                    a[1,2] <- 4
                    
                    
                    continue
                    
                end 
            elif (a==b) 
                abc()
            else 
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_272(self):
        """Simple program: int main() {} """
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 
                begin 
                break
                end     
                a <- 234 
            end 
            if (a+c) 
                begin
                    a[1,2] <- 4
                    continue
                end 
            elif (a==b) 
                abc()
            else 
            abc[1,2] <- true + false
            return a+b+c-a*abc(1,2,a) % a[1,2,3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
        
    def test_273(self):
        """Simple program: int main() {} """
        input = """func foo() return a+b+c-a*abc(1,2,a) % a[1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
        
    def test_274(self):
        """Simple program: int main() {} """
        input = """func foo() 
        return a+b+c-a*abc(1,2,a) % a[1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
        
    def test_275(self):
        """Simple program: int main() {} """
        input = """func foo() 
        
        
        return a+b+c-a*abc(1,2,a) % a[1,2,3]"""
        expect = "Error on line 4 col 44: <EOF>"
        self.assertTrue(TestParser.test(input,expect,275))
        
    def test_276(self):
        """Simple program: int main() {} """
        input = """func foo() begin
        
        abc(1,2,3)
        return a+b+c-a*abc(1,2,a) % a[1,2,3]
        end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
        
    def test_277(self):
        """Simple program: int main() {} """
        input = """func foo() 
        begin
        abc(1,2,"ditien",1+2,a[1,2,[2,3]])
        return a+b+c-a*abc(1,2,a) % a[1,2,3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
        
    def test_278(self):
        """Simple program: int main() {} """
        input = """func areDivisors(number num1, number num2)
                    return ((num1 % num2 = 0) or (num2 % num1 = 0))
                func main()
                    begin
                        var num1 <- readNumber()
                        var num2 <- readNumber()
                        if (areDivisors(num1, num2)) writeString("Yes")
                        else writeString("No")
                    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
        
    def test_279(self):
        """Simple program: int main() {} """
        input = """func isPrime(number x)
                func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) writeString("Yes")
                    else writeString("No")
                end
                func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                    if (x % i = 0) return false
                    end
                    return true
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    
    #
    def test_280(self):
        """Simple program: int main() {} """
        input = """
        func isPrime(number x)
                func main()
                begin
                    number x <- 2
                    if (isPrime(x)) writeString("Yes")
                    else writeString("No")
                end
                func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                    if (x % i = 0) return false
                    end
                    return true
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
        
    #
    def test_281(self):
        """Simple program: int main() {} """
        input = """##abcdieh
        func isPrime(number x)
                func main()
                begin
                    number x <- 2
                    if (isPrime(x)) writeString("Yes")
                    else writeString("No")
                end
                func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > (x / 2) by 1
                    begin
                    if (x % i = 0) return false
                    end
                    return (2+3)*a[1,2,3]
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
        
    def test_282(self):
        """Simple program: int main() {} """
        input = """func isPrime(number x)
                func main() ##abcdieh
                begin
                    number x <- 2 ##abcdieh
                    if (isPrime(x)) writeString("Yes")
                    ##abcdieh
                    else writeString("No")
                end
                func isPrime(number x)
                begin
                    if (x <= 1) return false
                    ##abcdieh
                    var i <- [2,4]
                    for i until i > (x / 2) by 1
                    begin
                    if (x % i = 0) return false
                    end
                    return (2+3)*a[1,2,3]
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
        
    def test_283(self):
        """Simple program: int main() {} """
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,283))
        
    def test_284(self):
        """Simple program: int main() {} """
        input = """string abc[1] <- [[1,2,8],[2,"asd",true,false]] 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
        
    def test_285(self):
        """Simple program: int main() {} """
        input = """func main() begin
        abc["rtien"] <- [[1,2,8],[2,"asd",true,false]] 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
        
    def test_286(self):
        """Simple program: int main() {} """
        input = """number abc["rtien"] <- [[1,2,y],[2,"asd",true,x]] 
        """
        expect = "Error on line 1 col 11: rtien"
        self.assertTrue(TestParser.test(input,expect,286))
        
    def test_287(self):
        """Simple program: int main() {} """
        input = """func main(string a[]) return  
        """
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input,expect,287))
        
    def test_288(self):
        """Simple program: int main() {} """
        input = """func main(string a) begin
        f()[0] <- 1
        return
        end  
        """
        expect = "Error on line 2 col 11: ["
        self.assertTrue(TestParser.test(input,expect,288))
        
    def test_289(self):
        """Simple program: int main() {} """
        input = """func main(string a) begin
        a[0] <- []
        return
        end  
        """
        expect = "Error on line 2 col 17: ]"
        self.assertTrue(TestParser.test(input,expect,289))
        
    def test_290(self):
        """Simple program: int main() {} """
        input = """func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
        
    def test_291(self):
        """Simple program: int main() {} """
        input = """func voi(number a, string b) begin
        var i <- 0
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
        
    def test_292(self):
        """Simple program: int main() {} """
        input = """func main() begin
        abc <- "nguyendaitien\i"
        end
        """
        expect = "nguyendaitien\i"
        self.assertTrue(TestParser.test(input,expect,292))
        
    def test_293(self):
        """Simple program: int main() {} """
        input = """func main() begin
        string s <- writeString("Hello this is a '"test'")
        end
        """
        expect = """Hello this is a '"test'")"""
        self.assertTrue(TestParser.test(input,expect,293))
        
    def test_294(self):
        """Simple program: int main() {} """
        input = """func main() begin
        string s <- "abc\ioao"
        end
        """
        expect = """abc\i"""
        self.assertTrue(TestParser.test(input,expect,294))
        
    def test_295(self):
        """Simple program: int main() {} """
        input = """func main() begin
        string s <- "abcahd
        end
        """
        expect = """abcahd"""
        self.assertTrue(TestParser.test(input,expect,295))
        
    def test_296(self):
        """Simple program: int main() {} """
        input = """func main() begin
        string s <- ???
        end
        """
        expect = """?"""
        self.assertTrue(TestParser.test(input,expect,296))

    def test_297(self):
        """Simple program: int main() {} """
        input = """var x ##this is an inline comment \n
        """
        expect = """Error on line 1 col 35: \n"""
        self.assertTrue(TestParser.test(input,expect,297))
        
    def test_298(self):
        """Simple program: int main() {} """
        input = """x <- 3
        """
        expect = """Error on line 1 col 0: x"""
        self.assertTrue(TestParser.test(input,expect,298))
        
    def test_299(self):
        """Simple program: int main() {} """
        input = """number a
        string _abc23 <- "ngyen dai tin"
        
        bool  Ad_2k3c <- false
        
        var AHDHD <- true
        
         
        dynamic k34533 <- 12.002E+234
        
        number A_adh0239[2,3,4,2] <- ["nguyen dai tien", 1, [1,2,3]]
        
        
        string __abcd[1]
        
        bool a[1,2,3] <- a/ not 2 * (3 == b % 4) ... (b == (c != d and 3 + 4 + 5 or 234) ... -abc(abc(), "nguyenditien")[cde(),"nguyen dait ein", true, false] )
        
        func _adhi24()
        func _afhi34(number abc, string cad, bool dhsj)
        
        
        func main() begin
            begin
            end
            
            number r
            number s <- not - a
            r <- 2.0
            number a[5,2,2]
            number b[5]
            s <- r * r * 3.14
            a[0] <- s + true - false
            
            number A_adh0239[2,3,4,2] <- ["nguyen dai tien", 1, [1,2,3]]
            
            if ((abc+e-2)) 
            begin
                if(true) return ## aefiefei
            end
            
            elif("nguye daiten") begin
                if(abc+234.2E34 * - 4e-2 ) e<-1+2
                elif(1) number k <- 2-2-3-4-4
                elif(abc) return ----2
                
                
            end ## aefiefei 
            
            else 
            begin
                if(abc+234.2E34 * - 4e-2 ) continue
                else break
                
                if(abc(1,tine,"tien",a[1,2,3])) 
                ngd(a["tien",12,bcd()],23,true,false,"tieh")
            end
            ## diatie
            
            begin
                for _sfs until abc() by abc()[1,2,3] begin
                    for i until abc()[1+2,2,3] by a[1] 
                    begin
                        if(true) begin
                            for i until i>1 by 3 break
                        end
                    end
                end
            end
            return abc
        end 
        
        func abc(string abc, number acdhi[1,2]) 
        return true
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,299))

