import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = """var str <- "Hello world!"
        """
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_302(self):
        input = """string a
        """
        expect = str(Program([VarDecl(Id("a"), StringType())]))
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test_303(self):
        input = """bool a
        """
        expect = str(Program([VarDecl(Id("a"), BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test_304(self):
        input = """dynamic a
        """
        expect = str(Program([VarDecl(Id("a"), None, "dynamic")]))
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test_305(self):
        input = """var b <- 3
        """
        expect = str(Program([VarDecl(Id("b"), None, "var", NumberLiteral(float(3)))]))
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test_306(self):
        input = """number b <- 57E2
        """
        expect = str(Program([VarDecl(Id("b"), NumberType(), None, NumberLiteral(float(57E2)))]))
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test_307(self):
        input = """var b <- true
        """
        expect = str(Program([VarDecl(Id("b"), None, "var", BooleanLiteral(True))]))
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_308(self):
        input = """string b <- 123e-123
        """
        expect = str(Program([VarDecl(Id("b"), StringType(), None, NumberLiteral(123e-123))]))
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_309(self):
        input = """string b <- 30.34
        """
        expect = str(Program([VarDecl(Id("b"), StringType(), None, NumberLiteral(30.34))]))
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test_310(self):
        input = """dynamic b <- 25.E-2
        """
        expect = str(Program([VarDecl(Id("b"), None, 'dynamic', NumberLiteral(25.E-2))]))
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_311(self):
        input = """bool b <- false
        """
        expect = str(Program([VarDecl(Id("b"), BoolType(), None, BooleanLiteral(False))]))
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_312(self):
        input = """bool b <- 16.23E+1
        """
        expect = str(Program([VarDecl(Id("b"), BoolType(), None, NumberLiteral(16.23E+1))]))
        self.assertTrue(TestAST.test(input, expect, 312))
    
    ###
    def test_313(self):
        input = """number a[1,2,3]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.,2.,3.],NumberType()))]))
        self.assertTrue(TestAST.test(input, expect, 313))
    
    ###
    def test_314(self):
        input = """string a[1,2.4,3]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.,2.4,3.],StringType()))]))
        self.assertTrue(TestAST.test(input, expect, 314))
        
    ###
    def test_315(self):
        input = """bool a[1,2,3e5]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.,2.,float(3e5)],BoolType()))]))
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_316(self):
        input = """number a <- a+b-1
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, BinaryOp("-", BinaryOp("+", Id("a"), Id("b")), NumberLiteral(1.)))]))
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_317(self):
        input = """number a <- "dai tien" ... "tien"
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, BinaryOp("...", StringLiteral("dai tien"), StringLiteral("tien")))]))
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_318(self):
        input = """dynamic __asd <- a and 123.e-123 or true
        """
        expect = str(Program([VarDecl(Id("__asd"), None, "dynamic", BinaryOp("or", BinaryOp("and", Id("a"), NumberLiteral(123.e-123)), BooleanLiteral(True)))]))
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test_319(self):
        input = """var A2a <- a == 123.e-123
        """
        expect = str(Program([VarDecl(Id("A2a"), None, "var", BinaryOp("==", Id("a"), NumberLiteral(123.e-123)))]))
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test_320(self):
        input = """var _A2a <- a * 123.e-123 * false % "eitn"
        """
        expect = str(Program([VarDecl(Id("_A2a"), None, "var", BinaryOp("%", BinaryOp("*", BinaryOp("*", Id("a"), NumberLiteral(123.e-123)), BooleanLiteral(False)), StringLiteral("eitn")))]))
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test_321(self):
        input = """bool True <- a + not b
        """
        expect = str(Program([VarDecl(Id("True"), BoolType(), None, BinaryOp("+", Id("a"), UnaryOp("not", Id("b"))))]))
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_322(self):
        input = """bool True <- a + - (not 5)
        """
        expect = str(Program([VarDecl(Id("True"), BoolType(), None, BinaryOp("+", Id("a"), UnaryOp("-", UnaryOp("not", NumberLiteral(5.)))))]))
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_323(self):
        input = """number False <- abcd()[3>=1]
        """
        expect = str(Program([VarDecl(Id("False"), NumberType(), None, ArrayCell(CallExpr(Id("abcd"),[]), [BinaryOp(">=", NumberLiteral(3.), NumberLiteral(1.))]))]))
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test_324(self):
        input = """number a <- ac[3>=1, -1]
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, ArrayCell(Id("ac"), [BinaryOp(">=", NumberLiteral(3.), NumberLiteral(1.)), UnaryOp("-", NumberLiteral(1.))]))]))
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_325(self):
        input = """number a <- ac(3>=1, -1)
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, CallExpr(Id("ac"), [BinaryOp(">=", NumberLiteral(3.), NumberLiteral(1.)), UnaryOp("-", NumberLiteral(1.))]))]))
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test_326(self):
        input = """string a <- [true, True, abc()]
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, ArrayLiteral([BooleanLiteral(True), Id("True"), CallExpr(Id("abc"),[])]))]))
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_327(self):
        input = """string a <- [[True], abc()["True"]] ##bachd
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, ArrayLiteral([ArrayLiteral([Id("True")]), ArrayCell(CallExpr(Id("abc"),[]), [StringLiteral("True")])]))]))
        self.assertTrue(TestAST.test(input, expect, 327))
        
    def test_328(self):
        input = """string a <- [[True], abc()["True"]] ##bachd
        number b <- a==c
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, ArrayLiteral([ArrayLiteral([Id("True")]), ArrayCell(CallExpr(Id("abc"),[]), [StringLiteral("True")])])), VarDecl(Id("b"), NumberType(), None, BinaryOp("==", Id("a"), Id("c")))]))
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test_329(self):
        input = """string a ##bachd
        
        
        number b <- a==c
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, None), VarDecl(Id("b"), NumberType(), None, BinaryOp("==", Id("a"), Id("c")))]))
        self.assertTrue(TestAST.test(input, expect, 329))
    
    
    def test_340(self):
        input = """func foo()
        """
        expect = str(Program([FuncDecl(Id("foo"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test_341(self):
        input = """func a(number a, string b)
        """
        expect = str(Program([FuncDecl(Id("a"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), StringType())], None)]))
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_342(self):
        input = """func _23(number a, bool b)
        """
        expect = str(Program([FuncDecl(Id("_23"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), BoolType())], None)]))
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_343(self):
        input = """func _23(bool b) return
        """
        expect = str(Program([FuncDecl(Id("_23"), [VarDecl(Id("b"), BoolType())], Return())]))
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_344(self):
        input = """func _23() return True
        """
        expect = str(Program([FuncDecl(Id("_23"), [], Return(Id("True")))]))
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test_345(self):
        input = """func A_23(number c[1,2]) return true
        """
        expect = str(Program([FuncDecl(Id("A_23"), [VarDecl(Id("c"), ArrayType([1.,2.], NumberType()))], Return(BooleanLiteral(True)))]))
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_346(self):
        input = """func A_23() return not abc() 
        """
        expect = str(Program([FuncDecl(Id("A_23"), [], Return(UnaryOp("not", CallExpr(Id("abc"), []))))]))
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_347(self):
        input = """func A_23() return 1+-2
        """
        expect = str(Program([FuncDecl(Id("A_23"), [], Return(BinaryOp("+", NumberLiteral(1.), UnaryOp("-", NumberLiteral(2.)))))]))
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_348(self):
        input = """func A_23() begin
        end
        """
        expect = str(Program([FuncDecl(Id("A_23"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_349(self):
        input = """func foo()
        begin
        number a <- a
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([VarDecl(Id("a"), NumberType(), None, Id("a"))]))]))
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test_350(self):
        input = """func foo(number c)
        begin
        number a <- a
        c <- 2
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([VarDecl(Id("a"), NumberType(), None, Id("a")), Assign(Id("c"), NumberLiteral(2.))]))]))
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test_351(self):
        input = """func foo(number c)
        begin
        c <- 2
        return c
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([Assign(Id("c"), NumberLiteral(2.)), Return(Id("c"))]))]))
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test_352(self):
        input = """func foo(number c)
        begin
        c <- 2
        break
        return c
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([Assign(Id("c"), NumberLiteral(2.)), Break(), Return(Id("c"))]))]))
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_353(self):
        input = """func foo(number c)
        begin
        c <- 2
        break
        continue
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([Assign(Id("c"), NumberLiteral(2.)), Break(), Continue()]))]))
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test_354(self):
        input = """func foo(number c)
        begin
        begin
        abc()
        end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([Block([CallStmt(Id("abc"), [])])]))]))
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_355(self):
        input = """func foo(number c)
        begin
        abc(1!=2,2>3)
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([CallStmt(Id("abc"), [BinaryOp("!=", NumberLiteral(1.), NumberLiteral(2.)), BinaryOp(">", NumberLiteral(2.), NumberLiteral(3.))])]))]))
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test_356(self):
        input = """func foo(number c)
        begin
            if (a+b) a <- b + 1
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), NumberType())], Block([If(BinaryOp("+", Id("a"), Id("b")), Assign(Id("a"), BinaryOp("+", Id("b"), NumberLiteral(1.))))]))]))
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test_357(self):
        input = """func foo(number c[1,2,3])
        begin
            if (a=b) a <- b < 1 
            elif (a>c) a[1,2] <- 4
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), ArrayType([1.,2.,3.], NumberType()))], Block([If(BinaryOp("=", Id("a"), Id("b")), Assign(Id("a"), BinaryOp("<", Id("b"), NumberLiteral(1.))), [(BinaryOp(">", Id("a"), Id("c")), Assign(ArrayCell(Id("a"), [NumberLiteral(1.), NumberLiteral(2.)]), NumberLiteral(4.)))])]))]))
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test_399(self):
        input = """ func inc(number a) return a + 1
                    func main() begin
                        var a <- 1
                        inc(a)
                        writeNumber(a)
                    end
                """
        expect = str(Program([FuncDecl(Id("inc"), [VarDecl(Id("a"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), NumberLiteral(1.0)))), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)), CallStmt(Id("inc"), [Id("a")]), CallStmt(Id("writeNumber"), [Id("a")])]))]))
        self.assertTrue(TestAST.test(input, expect, 399)) 