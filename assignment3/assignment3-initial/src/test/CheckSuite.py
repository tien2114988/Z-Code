import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """number a
        func b(number a, number a)
        begin 
        end
        """
        expect = str(Redeclared(Parameter(),'a'))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """number b
        string b
        number a
        """
        expect = str(Redeclared(Variable(), 'b'))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = """number a
        func b(number a, number a)
        func b(number a, number b)
        begin 
        end
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """number a
        func b(number a, number a)
        func b(number a, number a)
        begin 
        end
        """
        expect = str(Redeclared(Parameter(), 'a'))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
        bool a <- true
        func abc(string a) begin
        number a <- 3
        end
        func main()begin
        return
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """
        var a <- "tien"
        func main() begin
            number a <- 3
            string b
            begin
                bool b
                begin 
                    number b
                end
            end
        end
        number b
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
        func abc(string a, string a)
        func abc(string a, bool b) begin
        end
        number b
        """
        expect = str(Redeclared(Function(), 'abc'))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
        func main()begin
            number a <- readNumber()
        end
        func readNumber()
        """
        expect = str(Redeclared(Function(), 'readNumber'))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
        dynamic main <- 2
        func main() begin
            writeNumber(main)
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
        func foo(number a)
        func foo(number a)
        func main() return
        """
        expect = str(Redeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
        func foo(number a) 
            return a
        func foo(number a)
        func main() return
        """
        expect = str(Redeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
        func foo(number x, string y)

        func foo(number x, number x[1]) 
            begin
            end
        func main() return
        """
        expect = str(Redeclared(Parameter(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
        func foo(number x[2,3,4], string y[1,1,1])

        func foo(number x[2,3,4], string k[1,1]) 
            begin
            end
        func main() return
        """
        expect = str(Redeclared(Function(),'foo'))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
        func foo(number x[2,3,4], string y[1,1,1])

        func foo(number x[2,3,4], string k[1,1,1]) 
            begin
                dynamic c
            end
        func main() return
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
        func foo(number x[2,3,4], string y[1,1,1])

        func foo(number x[2,3,5], string k[1,1,1]) 
            begin
            end
        func main() return
        """
        expect = str(Redeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
        string a <- "2"
        func abc(string c, bool b) begin
            number e
            begin 
                number k
                begin
                    begin
                        a <- a ... "ee"
                    end
                end
                return e
            end 
            begin 
                return k
            end
        end
        """
        expect = str(Undeclared(Identifier(), 'k'))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
        func abc(string c, bool b) begin
            abcd()
        end
        """
        expect = str(Undeclared(Function(), 'abcd'))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
        func main ()                                       
        begin                                                   
            var i <- 1                                                     
            for i until i < 3 by 1                                 
                var x<-1                                                

            var y<- x    
            return                                           
        end                                                         
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
        func main ()                                       
        begin                                                   
            var i <- 1                                                     
            for i until i < 3 by 1  
            begin                               
                var x<-1                                                
            end
            var y<- x                                               
        end                                                         
        """
        expect = str(Undeclared(Identifier(), 'x'))
        self.assertTrue(TestChecker.test(input, expect, 418))


    def test_419(self):
        input = """
        func cd()
        func de()
        func abc(string c, bool b) begin
            bool b
            begin 
                dynamic c <- readNumber()
                c <- cd()
            end
        end
        """
        expect = str(NoDefinition('cd'))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
        func main()
        func cd()
        func abc(string c, bool b) begin
            bool b
            begin 
                dynamic c <- readNumber()
            end
        end
        """
        expect = str(NoDefinition('main'))
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
        bool a <- true
        func abc(string c, bool b) return a and b
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
        bool a <- true
        func main(string c, bool b) return a and b
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
        bool a <- true
        func main() return a
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
        bool k <- true
        func abc(string c, bool b) begin
            number a
            var b <- a
            dynamic c
            a <- c
            var d <- a + b + c - d % a / b * 2 + (-2)
            k <- d > b
            k <- d == k
        end
        """
        expect = str(TypeMismatchInExpression(BinaryOp('==',Id('d'),Id('k'))))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
        bool k <- true
        func abc(number e, number f) begin
            bool a
            var b <- a
            dynamic c
            a <- c
            var d <- not a and b or c and not d or (e <= f)
            k <- not d
            dynamic g <- g
        end
        """
        expect = str(TypeCannotBeInferred(VarDecl(Id('g'), None, 'dynamic', Id('g'))))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
        bool k <- true
        func abc(number e, number f) begin
            bool a
            var b <- a
            dynamic c
            a <- c
            string str <- str ... "s"
            dynamic str2 <- str 
            var d <- str == str2
            dynamic g <- str = str2
        end
        """
        expect = str(TypeMismatchInExpression(BinaryOp('=',Id('str'),Id('str2'))))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
        func main() begin
            number num
            dynamic num2 <- num
            var boo <- num = num2
            dynamic num3
            dynamic str 
            string str2 <- str
            boo <- (num != num2) and (num < num3) or (num2 > num) and not (num >= num2) or (num <= num3) and (str == str2)
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
        func main()
            begin
                dynamic num
                bool arr <- num and (num > num)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
        func main()
            begin
                dynamic num
                bool arr <- (- num != 3) and (num > num)
            end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
        func main()
            begin
                dynamic num <- (- num != 3) and (num > num)
            end
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(num), None, dynamic, BinaryOp(and, BinaryOp(!=, UnaryOp(-, Id(num)), NumLit(3.0)), BinaryOp(>, Id(num), Id(num))))'
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
        func main()
            begin
                var num <- (- num != 3) and (num > num)
            end
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(num), None, var, BinaryOp(and, BinaryOp(!=, UnaryOp(-, Id(num)), NumLit(3.0)), BinaryOp(>, Id(num), Id(num))))'
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = """
        func main()
            begin
                dynamic num 
                num <- (- num != 3) and (num > num)
            end
        end
        """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(num), BinaryOp(and, BinaryOp(!=, UnaryOp(-, Id(num)), NumLit(3.0)), BinaryOp(>, Id(num), Id(num))))'
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
        bool a[2,2] <- [[true,true],[false,true]]
        func a() return a[2+1,1]
        func main()begin
            dynamic a<- a()
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
        bool a <- true
        func a() return a[1,1]
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[NumberLiteral(1.), NumberLiteral(1.)])))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
        number a[2,2] <- [[1,1],[1,1]]
        dynamic c <- 2 - 4 + 1 / 3 * a[1,1]
        func main() begin
          var k <- a[1+2,c]
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
        number a[2,2] <- [[1,1],[1,1]]
        dynamic c <- 2 - 4 + 1 / 3 * a[c,1]
        func main() begin
          var k <- a[1+2,c<3]
        end
        """
        expect = 'Type Mismatch In Expression: ArrayCell(Id(a), [BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(<, Id(c), NumLit(3.0))])'
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
        number a[4] <- [1, true, false, "a"]
        """
        expect = 'Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True), BooleanLit(False), StringLit(a))'
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
        bool a <- true
        func a(number a, number b) return a

        func main() return a()

        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('a'),[])))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
        number a <- 2
        string c <- "ti"
        func a(number a, string b) return a

        func main() begin 
            var a <- a(a + 1 -4 ,c)
            number c <- a
        end

        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 439))


    def test_440(self):
        input = """
        number a <- 2
        string c <- "ti"
        func a(number a, string b) return a

        func main() begin 
            var a <- a(a,4+6 -3)
            number c <- a
        end
        """
        expect = 'Type Mismatch In Expression: CallExpr(Id(a), [Id(a), BinaryOp(-, BinaryOp(+, NumLit(4.0), NumLit(6.0)), NumLit(3.0))])'
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
        number a <- 2
        string c <- "ti"
        func a(number a, string b)begin
        end

        func main() begin 
            var a <- a(a + 1 -4 ,c)
            number c <- a
        end

        """
        expect = 'Type Mismatch In Expression: CallExpr(Id(a), [BinaryOp(-, BinaryOp(+, Id(a), NumLit(1.0)), NumLit(4.0)), Id(c)])'
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
        func main()begin
            number a[2,3] <- [[1,"1",1], [1,3,2]]
        end
        """
        expect = 'Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(1), NumLit(1.0))'
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
        func f()begin
            number c[3,2] <- [[6,7],[4,5],[4,5]]
            return c[2,0]
        end
        func main() begin
            number a <- f() 
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
        func main()begin
            number a[2,3] <- [[1,1], [1,2,2]]
        end
        """
        expect = 'Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(2.0)))'
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
        func main()begin
            number a[2,3] <- [[1,1,2], [true,true,true]]
        end
        """
        expect = 'Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0), NumLit(2.0)), ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(True)))'
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
        func foo()begin
        end
        func main()begin
            continue
        end
        """
        expect = str(MustInLoop(Continue()))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
        func foo()begin
        end
        func main()begin
            dynamic i
            for i until 2>3 by 2
            break
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
        func foo()begin
        end
        func main()begin
            dynamic i
            for i until 2>3 by 2
            begin
                if (i > 2)
                continue 
            end
            break
        end
        """
        expect = str(MustInLoop(Break()))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
        func foo()begin
        end
        func main()begin
            dynamic i
            for i until 2>3 by 2
            begin
                if (i > 2)
                for i until 2>3 by 2
                    continue 
                break
            end
            for i until 2>3 by 2
            begin
                if (i > 2)
                for i until 2>3 by 2
                    continue 
                break
            end
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
        func foo()begin
        end
        func main()begin
            dynamic x
            x <- (x = 1) or ("abc" == "abc")
        end
        """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))'
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
        func foo(number a)
        dynamic b
        dynamic c
        func foo(number a)begin
            if (b==c)
            return b
            elif ("tie" ... "g")
            return c
            else
            return a
        end
        func main()begin
            number a <- foo(1)
        end
        """
        expect = 'Type Mismatch In Statement: If((BinaryOp(==, Id(b), Id(c)), Return(Id(b))), [(BinaryOp(..., StringLit(tie), StringLit(g)), Return(Id(c)))], Return(Id(a)))'
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
        func foo(string a)
        dynamic b
        dynamic c
        func foo(string a)begin
            if (b+c)
            return b
            elif (a==b)
            return c
            else
            return a
        end
        func main()begin
            number a <- foo("1")
        end

        """
        expect = 'Type Mismatch In Statement: If((BinaryOp(+, Id(b), Id(c)), Return(Id(b))), [(BinaryOp(==, Id(a), Id(b)), Return(Id(c)))], Return(Id(a)))'
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
        func foo(string a)
        dynamic b
        dynamic c
        dynamic f
        func foo(string a)begin
            if (b>c)
            begin
                return a
            end
            elif (b<c)
            begin
                return f
            end
            else
            begin
                f <- b + c
            end
        end
        func main()begin
            number a <- foo("1")
        end

        """
        expect = str(TypeMismatchInStatement(Assign(Id('f'), BinaryOp('+', Id('b'), Id('c')))))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
        func main()begin
            number i
            dynamic a
            string b
            for i until a>2 by a
                b <- a ... "tien"
        end

        """
        expect = str(TypeMismatchInExpression(BinaryOp('...', Id('a'), StringLiteral("tien"))))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
        func main()begin
            string i
            dynamic a
            string b
            for i until a>2 by a
                b <- a ... "tien"
        end

        """
        expect = 'Type Mismatch In Statement: For(Id(i), BinaryOp(>, Id(a), NumLit(2.0)), Id(a), AssignStmt(Id(b), BinaryOp(..., Id(a), StringLit(tien))))'
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """
        func foo()
        func main()begin
            dynamic i
            dynamic a
            number c
            string b
            for i until foo() by a
                i <- c
            var e <- foo() and (i = c)
            for i until foo() by e
            return
        end
        func foo()begin
        end
        """
        expect = 'Type Mismatch In Statement: For(Id(i), CallExpr(Id(foo), []), Id(e), Return())'
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
        func boo(number c) return "tien"
        func foo(string a)
        dynamic b
        dynamic c
        dynamic f
        func foo(string a)begin
            if (b>c)
            begin
                return a
            end
            elif (b<c)
            begin
                return f
            end
            else
            begin
                for b until b!=c by b = c
                return
            end
        end
        func main()begin
        end
        """
        expect = 'Type Mismatch In Statement: For(Id(b), BinaryOp(!=, Id(b), Id(c)), BinaryOp(=, Id(b), Id(c)), Return())'
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """
        func main() begin
            dynamic b
            var a <- b + 1
            number c <- a - b
            c <- a <= b
        end
        """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(c), BinaryOp(<=, Id(a), Id(b)))'
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
        func main() begin
            dynamic b
            var a <- b + 1
            number c <- a - b
            dynamic e
            e <- (e=="tien") and (e + 2)
        end
        """
        expect = 'Type Mismatch In Expression: BinaryOp(+, Id(e), NumLit(2.0))'
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
        func main() begin
            dynamic b
            var a <- b + 1
            number c <- a - b
            dynamic e
            e <-  - (a + b / 2 - c % e * 45) + (e / 2)
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
        func main() begin
            number a[2,2]
            a <- [[1,3],[4,6]]
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """
        func main() begin
            number a[2,2]
            a <- [[1],[4]]
        end
        """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(ArrayLit(NumLit(1.0)), ArrayLit(NumLit(4.0))))'
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
        func main() begin
            number a[2,2]
            var b <- [[1,3],[4,6]]
            a <- b
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
        func main() begin
            number a[4]
            var b <- [true, true, false, false]
            a <- b
        end
        """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a), Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """
        func main() begin
            var b <- [true, true, false, false]
            dynamic c <- b
            c <- [true, false, false, false]
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = """
        func abc(number a)

        number a <- abc(7) + 1
        func main() begin
            abc(9)
        end
        """
        expect = 'Type Mismatch In Statement: CallStmt(Id(abc), [NumLit(9.0)])'
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """
        func abc(number a) return
        func main() begin
            abc(9)
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
        func abc(number a, string b) begin
        end
        func main() begin
            abc()
        end
        """
        expect = 'Type Mismatch In Statement: CallStmt(Id(abc), [])'
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
        func abc(number a, bool b) begin
        end
        func main() begin
            dynamic a
            abc(a, a > a)
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
        func abc(number a[3,2], bool b) begin
        end
        func main() begin
            dynamic a <- [[1,5], [4,5], [5,6]]
            abc(a, a[1,2] != a[2,1])
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
        func abc(number a[3,2]) begin
        end
        func main() begin
            dynamic a <- [[1,5], [4,5]]
            abc(a)
        end
        """
        expect = 'Type Mismatch In Statement: CallStmt(Id(abc), [Id(a)])'
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
        func abc(number a[3,2]) begin
        end
        func main() begin
            dynamic a <- [["1","5"], ["4","5"], ["5","6"]]
            abc(a)
        end
        """
        expect = 'Type Mismatch In Statement: CallStmt(Id(abc), [Id(a)])'
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
        func abc(number a[3,2]) begin
        end
        func main() begin
            number a <- ("tien" == "pd")
            abc(a)
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, BinaryOp(==, StringLit(tien), StringLit(pd)))'
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
        func abc(number a[3,2]) begin
        end
        func main() begin
            dynamic c <- [[2,3],[34,4],[5,4]]
            string a[3,2] <- c
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0, 2.0], StringType), None, Id(c))'
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
        func abc(number a[3,2]) begin
        end
        func main() begin
            string a[3] <- ["tien","few"]
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], StringType), None, ArrayLit(StringLit(tien), StringLit(few)))'
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """
        func foo(number a)
        dynamic b
        number a <- foo(2)
        func foo(number a)begin
            return b
        end
        func main()begin
            number k <- b
        end

        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
        func foo(number a)
        dynamic b
        dynamic c
        number a <- foo(2)
        func foo(number a)begin
            begin
                return b
            end
            begin
                return c
            end
            begin 
                bool k <- b>c
                begin 
                    return k
                end
            end
        end
        func main()begin
        end
        """
        expect = str(TypeMismatchInStatement(Return(Id('k'))))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """
        func foo(number a)
        func foo(number a)begin
            begin
                return 
            end
        end
        func main()begin
            number a <- foo(1)
        end

        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
        func foo(number a)
        func foo(number a)begin
            begin
            end
        end
        func main()begin
            number a <- foo(1)
        end

        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
        func foo(number a)
        func foo(number a)begin
            if (true)
                return true
            else
                return 1
        end
        func main()begin
            number a <- foo(1)
        end

        """
        expect = 'Type Mismatch In Statement: Return(NumLit(1.0))'
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
        func foo() begin
            return 1
            return "a"
        end
        func main() return
        """
        expect = str(TypeMismatchInStatement(Return(StringLiteral('a'))))
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
        func foo() begin
            return ["4","5","6"]
        end
        func main() begin
            number a[3] <- foo()
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, CallExpr(Id(foo), []))'
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """
        func foo() begin
            return [[4,5,6]]
        end
        func main() begin
            number a[1,3] <- foo()
        end
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
        func foo() begin
            return [[4,5,6]]
        end
        func main() begin
            number a[1,2] <- foo()
        end
        """
        expect = 'Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0], NumberType), None, CallExpr(Id(foo), []))'
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
        func main()
        begin
            dynamic a <- a
        end
        """
        expect = 'Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
        func main() begin
            dynamic b
            var a <- b
        end
        
        """
        expect = str(TypeCannotBeInferred(VarDecl(Id('a'), None, 'var', Id('b'))))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
        func main() begin
            var b <- 1+2
            dynamic a <- b
        end
        
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """
        dynamic a
        func foo() return a
        func main()
        begin
            number num <- foo()
        end
        """
        expect = 'Type Cannot Be Inferred: Return(Id(a))'
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
        func main()
        func foo()
        begin
            number a <- main()
        end
        func main() return 
        """
        expect = str(TypeMismatchInStatement(Return()))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
        func func1()
        func main()
        begin
        number a <- func1()
        end
        func func2()
        func func1()
        begin
        var b <- func2()
        return b
        end
        func func2() return 1
        """
        expect = 'Type Cannot Be Inferred: VarDecl(Id(b), None, var, CallExpr(Id(func2), []))'
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """
        func func1()
        func main()
        begin
        number a <- func1()
        end
        func func2()
        func func1()
        begin
        var b <- func2()
        return b
        end
        func func2() return 1
        """
        expect = 'Type Cannot Be Inferred: VarDecl(Id(b), None, var, CallExpr(Id(func2), []))'
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
        func foo()
        func main()
        begin
            dynamic a
            var b <- (foo() + a * foo() / b) - (a % b)
            dynamic c 
            c <- not c and (c or false)
            dynamic e <- e ... "tien"
            var g <- (e == "e") and (a > b) or (b >= foo()) and (a <= foo()) or (a < b) and (foo() != foo())
            var f <- f
        end
        """
        expect = 'Type Cannot Be Inferred: VarDecl(Id(f), None, var, Id(f))'
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
        func foo(number a, string b)
        func boo()
        func main()
        begin
            dynamic a <- [[3,4,8],[4,6,7]]
            dynamic b
            dynamic c
            var d <- a[b,foo(c, "c")]
        end
        func foo(number a, string b)begin
            dynamic c
            c <- boo()
        end
        """
        expect = 'Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(boo), []))'
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
        func foo(number a, string b)
        func boo()
        begin
            dynamic a
            dynamic b
            dynamic c
            dynamic d
            if (a) begin
                var a <- [[1]]
                return a
            end
            elif (b) return c
            else begin
                d <- a and b
                d <- c[0,0] != c[0,0]
            end
        end
        func foo(number a, string b)begin
            dynamic b 
            return b
        end 
        func main() return
        """
        expect = 'Type Cannot Be Inferred: Return(Id(b))'
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
        func boo()
        begin
            dynamic a
            dynamic b
            dynamic c
            dynamic d
            for a until b by c
            begin
                var d <- a > c 
                var e <- d or b
            end
            return d
        end
        func main() return
        """
        expect = 'Type Cannot Be Inferred: Return(Id(d))'
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
        func boo()
        func main() return boo()
        """
        expect = 'Type Cannot Be Inferred: Return(CallExpr(Id(boo), []))'
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
        func boo(number a)
        func main() begin
            dynamic b
            boo(boo(b))
            b <- boo(b)
        end
        """
        expect = 'Type Mismatch In Expression: CallExpr(Id(boo), [Id(b)])'
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
        func boo(string a)
        func main() begin
            dynamic b
            b <- boo(boo(b))
            b <- boo(b)
        end
        func boo(string a) return a
        """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 499))

    
     
       
    
        



