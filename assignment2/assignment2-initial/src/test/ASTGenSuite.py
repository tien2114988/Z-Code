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
        
    def test_330(self):
        input = """

        number a[4,5] 

        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([4.0, 5.0], NumberType()), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test_331(self):
        input = """
        string b
        number a[4,5]
        bool k
        """
        expect = str(Program([
                        VarDecl(Id("b"), StringType()),
                        VarDecl(Id("a"), ArrayType([4., 5.], NumberType())),
                        VarDecl(Id("k"), BoolType())
                    ]))
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test_332(self):
        input = """
        func abc()
        number a[4,5]
        bool k
        """
        expect = str(Program([
                        FuncDecl(Id("abc"), []),
                        VarDecl(Id("a"), ArrayType([4., 5.], NumberType())),
                        VarDecl(Id("k"), BoolType())
                    ]))
        self.assertTrue(TestAST.test(input, expect, 332))
        
    def test_333(self):
        input = """number a <-  not a and -2 ... a != abc(3) 
        """
        expect = str(Program([
                        VarDecl(Id("a"), 
                                NumberType(),
                                None,
                                BinaryOp("...",
                                         BinaryOp("and",
                                                UnaryOp("not", Id("a")),
                                                UnaryOp("-", NumberLiteral(2.)
                                                )),
                                         BinaryOp("!=",
                                                  Id("a"),
                                                  CallExpr(Id("abc"), [NumberLiteral(3.)])
                                         )
                                )  
                            )]))
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_334(self):
        input = """number a <- a[b[c["toan",2],true],"tien"] 
        """
        expect = str(Program([
                        VarDecl(Id("a"), 
                                NumberType(),
                                None,
                                ArrayCell(Id("a"),
                                         [
                                            ArrayCell(
                                                Id("b"),
                                                [
                                                    ArrayCell(Id("c"),
                                                              [StringLiteral("toan"), NumberLiteral(2.)]
                                                        ),
                                                    BooleanLiteral(True)
                                                ]
                                            ),
                                            StringLiteral("tien")
                                         ]
                                         )
                                 
                            )]))
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test_335(self):
        input = """dynamic a <- ("tine" ... "fa") + 2 
        """
        expect = str(Program([
                        VarDecl(Id("a"), 
                                None,
                                "dynamic",
                                BinaryOp("+", BinaryOp("...", StringLiteral("tine"), StringLiteral("fa")), NumberLiteral(2.))
                            )]))
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test_336(self):
        input = '''
func Ska ()	return
func JJ84 ()	return
bool ssX[11.76]
func wt (bool Kec, bool Wa)
	return 14.33
dynamic xGo5 <- tU
'''
        expect = '''Program([FuncDecl(Id(Ska), [], Return()), FuncDecl(Id(JJ84), [], Return()), VarDecl(Id(ssX), ArrayType([11.76], BoolType), None, None), FuncDecl(Id(wt), [VarDecl(Id(Kec), BoolType, None, None), VarDecl(Id(Wa), BoolType, None, None)], Return(NumLit(14.33))), VarDecl(Id(xGo5), None, dynamic, Id(tU))])'''
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_337(self):
        input = '''
func Qu (bool Jw[9.22,67.94,19.3], string bMv[44.19,54.7], number B8DX)	return
'''
        expect = '''Program([FuncDecl(Id(Qu), [VarDecl(Id(Jw), ArrayType([9.22, 67.94, 19.3], BoolType), None, None), VarDecl(Id(bMv), ArrayType([44.19, 54.7], StringType), None, None), VarDecl(Id(B8DX), NumberType, None, None)], Return())])'''
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_338(self):
        input = '''
func oFyz ()
	begin
		string GYt6
	end

'''
        expect = '''Program([FuncDecl(Id(oFyz), [], Block([VarDecl(Id(GYt6), StringType, None, None)]))])'''
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_339(self):
        input = '''
func Ot (number qr[58.25,12.82], string XOe, number kbgL)	return
func uA0H ()
	return "tAB"

dynamic NZ
'''
        expect = '''Program([FuncDecl(Id(Ot), [VarDecl(Id(qr), ArrayType([58.25, 12.82], NumberType), None, None), VarDecl(Id(XOe), StringType, None, None), VarDecl(Id(kbgL), NumberType, None, None)], Return()), FuncDecl(Id(uA0H), [], Return(StringLit(tAB))), VarDecl(Id(NZ), None, dynamic, None)])'''
        self.assertTrue(TestAST.test(input, expect, 339))
        
    
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
        
    def test_358(self):
        input = """func foo()
        begin
            if (a>=b) number a
            
            elif (a<=c) 
            
            a[1,2] <- 4
            
            elif (a...b) 
            abc()
            
            
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([If(BinaryOp(">=", Id("a"), Id("b")), VarDecl(Id("a"), NumberType(), None, None), [(BinaryOp("<=", Id("a"), Id("c")), Assign(ArrayCell(Id("a"), [NumberLiteral(1.), NumberLiteral(2.)]), NumberLiteral(4.))), (BinaryOp("...", Id("a"), Id("b")), CallStmt(Id("abc"), []))])]))]))
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_359(self):
        input = """func foo()
        begin
            if (-2) bool a
            
            elif (not true) 
            
            a[1,2] <- 4
            
            elif (a...b) 
            abc()
            else
            
            abc[1,2] <- true + false
        end
        
        
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([If(UnaryOp("-", NumberLiteral(2.)), VarDecl(Id("a"), BoolType(), None, None), [(UnaryOp("not", BooleanLiteral(True)), Assign(ArrayCell(Id("a"), [NumberLiteral(1.), NumberLiteral(2.)]), NumberLiteral(4.))), (BinaryOp("...", Id("a"), Id("b")), CallStmt(Id("abc"), []))], Assign(ArrayCell(Id("abc"), [NumberLiteral(1.), NumberLiteral(2.)]), BinaryOp("+", BooleanLiteral(True), BooleanLiteral(False))))]))]))
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test_360(self):
        input = """func foo()
        begin
            if (0) 
            begin
            break
            end
            else 
            
            continue
        end
        
        
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [], 
                Block(
                    [If(
                        NumberLiteral(0.), 
                        Block([Break()]), 
                        [], 
                        Continue())
                    ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test_361(self):
        input = """func foo()
        begin
            begin 
                for abcd until abcd >= efgh by 1233 
                a <- true
            end 
            
        end
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [], 
                Block(
                    [Block([
                        For(
                            Id("abcd"),
                            BinaryOp(">=", Id("abcd"), Id("efgh")),
                            NumberLiteral(1233.),
                            Assign(Id("a"), BooleanLiteral(True))
                        )
                    ])
                    ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test_362(self):
        input = """func foo(string s)
        begin
                for i until i != "i" by i ... "k" 
                begin
                continue
                end
        end
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [
                    VarDecl(Id("s"), StringType())
                ], 
                Block([
                    For(
                        Id("i"),
                        BinaryOp("!=", Id("i"), StringLiteral("i")),
                        BinaryOp("...", Id("i"), StringLiteral("k")),
                        Block(
                            [Continue()]
                        )
                    )
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """func foo(string s)
        begin
                for i until not i by -i
                begin
                if(a) string b
                end
        end
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [
                    VarDecl(Id("s"), StringType())
                ], 
                Block([
                    For(
                        Id("i"),
                        UnaryOp("not", Id("i")),
                        UnaryOp("-", Id("i")),
                        Block(
                            [If(Id("a"), VarDecl(Id("b"), StringType()))]
                        )
                    )
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test_364(self):
        input = """func foo()
        begin
            begin 
            number a
            end 
            if (a+c) 
            begin
            a[1,2] <- 4
            end 
            elif (a==b) 
            abc()
        end
        
        
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [], 
                Block([
                    Block([VarDecl(Id("a"), NumberType())]),
                    If(
                        BinaryOp("+", Id("a"), Id("c")),
                        Block([Assign(ArrayCell(Id("a"), [NumberLiteral(1.), NumberLiteral(2.)]), NumberLiteral(4.))]),
                        [(BinaryOp("==", Id("a"), Id("b")), CallStmt(Id("abc"), []))]
                    )
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test_365(self):
        input = """func foo()
        begin
            begin 
            end 
            begin
            end 
        end
        
        
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [], 
                Block([
                    Block([]),
                    Block([])
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test_366(self):
        input = """func foo()
        begin
            begin 
                begin
                end
            end 
            begin
                return 
            end 
        end
        
        
        """
        expect = str(Program(
            [FuncDecl(
                Id("foo"), 
                [], 
                Block([
                    Block([Block([])]),
                    Block([Return()])
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test_367(self):
        input = """func isPrime(number x)
                    begin
                        if (x <= 1) return false
                        var i <- 2
                        for i until i > - x by 1
                        begin
                            if (x % i = 0) return false
                        end
                        return true
                    end
        """
        expect = str(Program(
            [FuncDecl(
                Id("isPrime"), 
                [VarDecl(Id("x"), NumberType())], 
                Block([
                    If(BinaryOp("<=", Id("x"), NumberLiteral(1.)), Return(BooleanLiteral(False))),
                    VarDecl(Id("i"), None, "var", NumberLiteral(2.)),
                    For(
                        Id("i"), 
                        BinaryOp(">", Id("i"), UnaryOp("-", Id("x"))),
                        NumberLiteral(1.),
                        Block([If(BinaryOp("=",BinaryOp("%", Id("x"), Id("i")) , NumberLiteral(0.)), Return(BooleanLiteral(False)))])
                        ),
                    Return(BooleanLiteral(True))
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test_368(self):
        input = """func isPrime(number x)
                    begin
                        ## bahc
                        ## aefgu
                        ## hsh
                    end
        """
        expect = str(Program(
            [FuncDecl(
                Id("isPrime"), 
                [VarDecl(Id("x"), NumberType())], 
                Block([]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test_369(self):
        input = """func isPrime(number x)
                    begin
                        ## bahc
                        ## aefgu
                        a <- "\'"bcd\'""
                        ## hsh
                    end
        """
        expect = str(Program(
            [FuncDecl(
                Id("isPrime"), 
                [VarDecl(Id("x"), NumberType())], 
                Block([Assign(Id("a"), StringLiteral('\'"bcd\'"'))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test_370(self):
        input = """func isPrime(number x)
                    begin
                        ## bahc
                        ## aefgu
                        a <- "bcd\fsd"
                        ## hsh
                    end
        """
        expect = str(Program(
            [FuncDecl(
                Id("isPrime"), 
                [VarDecl(Id("x"), NumberType())], 
                Block([Assign(Id("a"), StringLiteral("bcd\fsd"))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test_371(self):
        input = """number a
        string b
        func isPrime(number x)
                    begin
                        ## bahc
                        ## aefgu
                        a <- "bcd\fsd"
                        ## hsh
                    end
        """
        expect = str(Program(
            [   
                VarDecl(Id("a"), NumberType()),
                VarDecl(Id("b"), StringType()),
                FuncDecl(
                Id("isPrime"), 
                [VarDecl(Id("x"), NumberType())], 
                Block([Assign(Id("a"), StringLiteral("bcd\fsd"))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test_372(self):
        input = """number a
        func isPrime()
        func isPrime(number x)
                    begin
                        ## bahc
                        ## aefgu
                        a <- "bcd\fsd"
                        ## hsh
                    end
        
        """
        expect = str(Program(
            [   
                VarDecl(Id("a"), NumberType()),
                FuncDecl(Id("isPrime"), []),
                FuncDecl(
                Id("isPrime"), 
                [VarDecl(Id("x"), NumberType())], 
                Block([Assign(Id("a"), StringLiteral("bcd\fsd"))]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 372))
        
    def test_373(self):
        input = """var a <- 2e+10
        func isPrime()
        ## bahc
        ## aefgu
        func isPrime()
                    begin
                        
                        a <- "bcd\fsd"
                        ## hsh
                    end
        func main() return
        """
        expect = str(Program(
            [   
                VarDecl(Id("a"), None, "var", NumberLiteral(float(2e+10))),
                FuncDecl(Id("isPrime"), []),
                FuncDecl(
                    Id("isPrime"), 
                    [], 
                    Block([Assign(Id("a"), StringLiteral("bcd\fsd"))])),
                FuncDecl(Id("main"), [], Return())
            ]))
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test_374(self):
        input = '''
func PpV (number BL, string zg6w[26.28,6.16], bool lTcW)	return AQtY

number v2
'''
        expect = '''Program([FuncDecl(Id(PpV), [VarDecl(Id(BL), NumberType, None, None), VarDecl(Id(zg6w), ArrayType([26.28, 6.16], StringType), None, None), VarDecl(Id(lTcW), BoolType, None, None)], Return(Id(AQtY))), VarDecl(Id(v2), NumberType, None, None)])'''
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test_375(self):
        input = '''
func CPp (string Bw[13.61,38.33], string qzR8)
	return 97.21

'''
        expect = '''Program([FuncDecl(Id(CPp), [VarDecl(Id(Bw), ArrayType([13.61, 38.33], StringType), None, None), VarDecl(Id(qzR8), StringType, None, None)], Return(NumLit(97.21)))])'''
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test_376(self):
        input = '''
bool P7
'''
        expect = '''Program([VarDecl(Id(P7), BoolType, None, None)])'''
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test_377(self):
        input = '''
func WJ (number iE[27.45], string nln[76.62,36.85], number gTQ[84.36,36.11])
	return 21.3
func XHb (bool ceX[21.78], bool K2[47.88,91.93], bool uc)	begin
		WC[60.68, HZ] <- "abVJc"
		CqV <- "ioL"
		bool Pg4
	end

string otx[47.29,53.16] <- Q729
func lq (bool fz, string Fs8K[97.48])	return bB
bool y4 <- n9d
'''
        expect = '''Program([FuncDecl(Id(WJ), [VarDecl(Id(iE), ArrayType([27.45], NumberType), None, None), VarDecl(Id(nln), ArrayType([76.62, 36.85], StringType), None, None), VarDecl(Id(gTQ), ArrayType([84.36, 36.11], NumberType), None, None)], Return(NumLit(21.3))), FuncDecl(Id(XHb), [VarDecl(Id(ceX), ArrayType([21.78], BoolType), None, None), VarDecl(Id(K2), ArrayType([47.88, 91.93], BoolType), None, None), VarDecl(Id(uc), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(WC), [NumLit(60.68), Id(HZ)]), StringLit(abVJc)), AssignStmt(Id(CqV), StringLit(ioL)), VarDecl(Id(Pg4), BoolType, None, None)])), VarDecl(Id(otx), ArrayType([47.29, 53.16], StringType), None, Id(Q729)), FuncDecl(Id(lq), [VarDecl(Id(fz), BoolType, None, None), VarDecl(Id(Fs8K), ArrayType([97.48], StringType), None, None)], Return(Id(bB))), VarDecl(Id(y4), BoolType, None, Id(n9d))])'''
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test_378(self):
        input = '''
func Pw (string Hf[5.42,77.56])
	return "KdOHe"
func Dk ()
	return

'''
        expect = '''Program([FuncDecl(Id(Pw), [VarDecl(Id(Hf), ArrayType([5.42, 77.56], StringType), None, None)], Return(StringLit(KdOHe))), FuncDecl(Id(Dk), [], Return())])'''
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test_379(self):
        input = '''
string PF <- vbnM
func xT ()
	return false

'''
        expect = '''Program([VarDecl(Id(PF), StringType, None, Id(vbnM)), FuncDecl(Id(xT), [], Return(BooleanLit(False)))])'''
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test_380(self):
        input = '''
var nO <- 67.98
string yF <- 60.76
func Mo ()
	return
dynamic PyH
'''
        expect = '''Program([VarDecl(Id(nO), None, var, NumLit(67.98)), VarDecl(Id(yF), StringType, None, NumLit(60.76)), FuncDecl(Id(Mo), [], Return()), VarDecl(Id(PyH), None, dynamic, None)])'''
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test_381(self):
        input = '''
func AjL (number OH[92.65,96.82])	begin
		Qph <- R9n
		string aakY <- 41.19
	end
'''
        expect = '''Program([FuncDecl(Id(AjL), [VarDecl(Id(OH), ArrayType([92.65, 96.82], NumberType), None, None)], Block([AssignStmt(Id(Qph), Id(R9n)), VarDecl(Id(aakY), StringType, None, NumLit(41.19))]))])'''
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test_382(self):
        input = '''
func erDI ()	return
string UR_
func jf0 (number x97)
	return

func Sn99 (bool Cmoi[11.99])
	begin
		for Vc until "OwBIM" by TrtK
			break
		return false
		break
	end

'''
        expect = '''Program([FuncDecl(Id(erDI), [], Return()), VarDecl(Id(UR_), StringType, None, None), FuncDecl(Id(jf0), [VarDecl(Id(x97), NumberType, None, None)], Return()), FuncDecl(Id(Sn99), [VarDecl(Id(Cmoi), ArrayType([11.99], BoolType), None, None)], Block([For(Id(Vc), StringLit(OwBIM), Id(TrtK), Break), Return(BooleanLit(False)), Break]))])'''
        self.assertTrue(TestAST.test(input, expect, 382))
        
    def test_383(self):
        input = '''
func erDI ()	return
string UR_
func jf0 (number x97)
	return

func Sn99 (bool Cmoi[11.99])
	begin
		for Vc until "OwBIM" by TrtK
			break
		return false
		break
	end

'''
        expect = '''Program([FuncDecl(Id(erDI), [], Return()), VarDecl(Id(UR_), StringType, None, None), FuncDecl(Id(jf0), [VarDecl(Id(x97), NumberType, None, None)], Return()), FuncDecl(Id(Sn99), [VarDecl(Id(Cmoi), ArrayType([11.99], BoolType), None, None)], Block([For(Id(Vc), StringLit(OwBIM), Id(TrtK), Break), Return(BooleanLit(False)), Break]))])'''
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test_384(self):
        input = '''
number Y4[24.14] <- RB8f
bool O_[22.61] <- true
func dGq ()
	begin
		lnA <- 28.37
		continue
	end
func OB (string roL[42.67,47.25], string usV6[28.79,40.2])
	return

func RtWQ (string Ri[55.26], number sC6[95.41,57.64,63.79])
	return
'''
        expect = '''Program([VarDecl(Id(Y4), ArrayType([24.14], NumberType), None, Id(RB8f)), VarDecl(Id(O_), ArrayType([22.61], BoolType), None, BooleanLit(True)), FuncDecl(Id(dGq), [], Block([AssignStmt(Id(lnA), NumLit(28.37)), Continue])), FuncDecl(Id(OB), [VarDecl(Id(roL), ArrayType([42.67, 47.25], StringType), None, None), VarDecl(Id(usV6), ArrayType([28.79, 40.2], StringType), None, None)], Return()), FuncDecl(Id(RtWQ), [VarDecl(Id(Ri), ArrayType([55.26], StringType), None, None), VarDecl(Id(sC6), ArrayType([95.41, 57.64, 63.79], NumberType), None, None)], Return())])'''
        self.assertTrue(TestAST.test(input, expect, 384))
    
    def test_385(self):
        input = '''
func MQqt (string lmy[75.57,19.4])
	return
func Cj4M (bool Ia, bool VLcU, bool dk8[80.13])
	return 22.44

func YeC ()	begin
		continue
	end

number ci1J[89.89,35.37]
'''
        expect = '''Program([FuncDecl(Id(MQqt), [VarDecl(Id(lmy), ArrayType([75.57, 19.4], StringType), None, None)], Return()), FuncDecl(Id(Cj4M), [VarDecl(Id(Ia), BoolType, None, None), VarDecl(Id(VLcU), BoolType, None, None), VarDecl(Id(dk8), ArrayType([80.13], BoolType), None, None)], Return(NumLit(22.44))), FuncDecl(Id(YeC), [], Block([Continue])), VarDecl(Id(ci1J), ArrayType([89.89, 35.37], NumberType), None, None)])'''
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test_386(self):
        input = '''
func jD (bool IF[52.75])	return 63.64
number WsC[39.72,17.78,54.43] <- 70.13
func nr ()	return

'''
        expect = '''Program([FuncDecl(Id(jD), [VarDecl(Id(IF), ArrayType([52.75], BoolType), None, None)], Return(NumLit(63.64))), VarDecl(Id(WsC), ArrayType([39.72, 17.78, 54.43], NumberType), None, NumLit(70.13)), FuncDecl(Id(nr), [], Return())])'''
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test_387(self):
        input = '''
string lg[68.0,19.0,65.93] <- 55.78
func GZm ()
	begin
		yRAS(VXX, 34.77, "S")
	end

'''
        expect = '''Program([VarDecl(Id(lg), ArrayType([68.0, 19.0, 65.93], StringType), None, NumLit(55.78)), FuncDecl(Id(GZm), [], Block([CallStmt(Id(yRAS), [Id(VXX), NumLit(34.77), StringLit(S)])]))])'''
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test_388(self):
        input = '''
func L4 ()
	return EH__

var q8uH <- 21.93
'''
        expect = '''Program([FuncDecl(Id(L4), [], Return(Id(EH__))), VarDecl(Id(q8uH), None, var, NumLit(21.93))])'''
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test_389(self):
        input = '''
string isp <- false
number ReM <- true
var Nr <- "F"
func Cw ()
	return "yllkw"

'''
        expect = '''Program([VarDecl(Id(isp), StringType, None, BooleanLit(False)), VarDecl(Id(ReM), NumberType, None, BooleanLit(True)), VarDecl(Id(Nr), None, var, StringLit(F)), FuncDecl(Id(Cw), [], Return(StringLit(yllkw)))])'''
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test_390(self):
        input = '''
number Ews
bool DLpA[34.9,22.73]
func ZN (bool aB, number xID)
	begin
		begin
			Rb(false)
		end
		return "lbt"
		gP_[BDQ, 89.86] <- true
	end
func aXju (bool yq[38.05,42.04])
	return 65.15

'''
        expect = '''Program([VarDecl(Id(Ews), NumberType, None, None), VarDecl(Id(DLpA), ArrayType([34.9, 22.73], BoolType), None, None), FuncDecl(Id(ZN), [VarDecl(Id(aB), BoolType, None, None), VarDecl(Id(xID), NumberType, None, None)], Block([Block([CallStmt(Id(Rb), [BooleanLit(False)])]), Return(StringLit(lbt)), AssignStmt(ArrayCell(Id(gP_), [Id(BDQ), NumLit(89.86)]), BooleanLit(True))])), FuncDecl(Id(aXju), [VarDecl(Id(yq), ArrayType([38.05, 42.04], BoolType), None, None)], Return(NumLit(65.15)))])'''
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test_391(self):
        input = '''
string oNN[83.45]
bool yd[12.34] <- false
func i4 ()
	begin
		eD <- "oEBi"
	end

'''
        expect = '''Program([VarDecl(Id(oNN), ArrayType([83.45], StringType), None, None), VarDecl(Id(yd), ArrayType([12.34], BoolType), None, BooleanLit(False)), FuncDecl(Id(i4), [], Block([AssignStmt(Id(eD), StringLit(oEBi))]))])'''
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test_392(self):
        input = '''
string D6zL
func VYt ()	return PI

func yE (bool iuP, number kT[16.12,31.44,99.77], number jCo0)
	return

string pPjw[18.91,13.69] <- "CYU"
'''
        expect = '''Program([VarDecl(Id(D6zL), StringType, None, None), FuncDecl(Id(VYt), [], Return(Id(PI))), FuncDecl(Id(yE), [VarDecl(Id(iuP), BoolType, None, None), VarDecl(Id(kT), ArrayType([16.12, 31.44, 99.77], NumberType), None, None), VarDecl(Id(jCo0), NumberType, None, None)], Return()), VarDecl(Id(pPjw), ArrayType([18.91, 13.69], StringType), None, StringLit(CYU))])'''
        self.assertTrue(TestAST.test(input, expect, 392))
        
    def test_393(self):
        input = '''
func P1i3 ()	return
func kE0 (bool Sdg, number AC[66.86,81.44,11.89])	return

func mF ()
	return
'''
        expect = '''Program([FuncDecl(Id(P1i3), [], Return()), FuncDecl(Id(kE0), [VarDecl(Id(Sdg), BoolType, None, None), VarDecl(Id(AC), ArrayType([66.86, 81.44, 11.89], NumberType), None, None)], Return()), FuncDecl(Id(mF), [], Return())])'''
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test_394(self):
        input = '''
bool Wrv <- h9RI
var lz <- false
'''
        expect = '''Program([VarDecl(Id(Wrv), BoolType, None, Id(h9RI)), VarDecl(Id(lz), None, var, BooleanLit(False))])'''
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test_395(self):
        input = '''
func LK (bool bnBM[67.1,10.48], number yj)	return 30.05
func gT (bool Cm[97.42,84.75,31.19])	begin
	end
'''
        expect = '''Program([FuncDecl(Id(LK), [VarDecl(Id(bnBM), ArrayType([67.1, 10.48], BoolType), None, None), VarDecl(Id(yj), NumberType, None, None)], Return(NumLit(30.05))), FuncDecl(Id(gT), [VarDecl(Id(Cm), ArrayType([97.42, 84.75, 31.19], BoolType), None, None)], Block([]))])'''
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test_396(self):
        input = '''
string kUdC
func Q5pR (bool JT_Z, bool WUvI[52.94,18.54])
	begin
	end

func vvL (number Df4[24.66])
	return
string BF[19.67,19.4,42.49]
'''
        expect = '''Program([VarDecl(Id(kUdC), StringType, None, None), FuncDecl(Id(Q5pR), [VarDecl(Id(JT_Z), BoolType, None, None), VarDecl(Id(WUvI), ArrayType([52.94, 18.54], BoolType), None, None)], Block([])), FuncDecl(Id(vvL), [VarDecl(Id(Df4), ArrayType([24.66], NumberType), None, None)], Return()), VarDecl(Id(BF), ArrayType([19.67, 19.4, 42.49], StringType), None, None)])'''
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test_397(self):
        input = '''
number kub[63.48,12.07,31.95] <- wZ
number DKi3[31.27]
func cKyo (string UJ[9.41,94.76,43.09])
	return
func A3 (bool t0p[8.67,51.64], bool x7KI[59.71])
	return bu
func f8 (bool XuT8[66.69,41.4], string xnj)
	begin
		begin
			kF(b5Y, false)
			for Sxv until 46.09 by false
				mng7 <- "YRX"
			VDX(89.07)
		end
	end
'''
        expect = '''Program([VarDecl(Id(kub), ArrayType([63.48, 12.07, 31.95], NumberType), None, Id(wZ)), VarDecl(Id(DKi3), ArrayType([31.27], NumberType), None, None), FuncDecl(Id(cKyo), [VarDecl(Id(UJ), ArrayType([9.41, 94.76, 43.09], StringType), None, None)], Return()), FuncDecl(Id(A3), [VarDecl(Id(t0p), ArrayType([8.67, 51.64], BoolType), None, None), VarDecl(Id(x7KI), ArrayType([59.71], BoolType), None, None)], Return(Id(bu))), FuncDecl(Id(f8), [VarDecl(Id(XuT8), ArrayType([66.69, 41.4], BoolType), None, None), VarDecl(Id(xnj), StringType, None, None)], Block([Block([CallStmt(Id(kF), [Id(b5Y), BooleanLit(False)]), For(Id(Sxv), NumLit(46.09), BooleanLit(False), AssignStmt(Id(mng7), StringLit(YRX))), CallStmt(Id(VDX), [NumLit(89.07)])])]))])'''
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test_398(self):
        input = '''
func LSf (bool bb, number TqA[34.73,9.9,28.48])	return
dynamic hjZ
var nUCI <- 9.84
'''
        expect = '''Program([FuncDecl(Id(LSf), [VarDecl(Id(bb), BoolType, None, None), VarDecl(Id(TqA), ArrayType([34.73, 9.9, 28.48], NumberType), None, None)], Return()), VarDecl(Id(hjZ), None, dynamic, None), VarDecl(Id(nUCI), None, var, NumLit(9.84))])'''
        self.assertTrue(TestAST.test(input, expect, 398))

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


