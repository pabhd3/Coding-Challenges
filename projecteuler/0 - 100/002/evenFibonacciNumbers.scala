object evenFibonacciNumbersSum {
    def generateFibonacci(n: String): Int = {
        // Generate the sequence
        var fib = List(1, 1)
        def isEven(i: Int): Boolean = i % 2 == 0
        for(i <- 0 to n.toInt) {
            val l = fib.length
            if(fib(l-1) + fib(l-2) > n.toInt) {
                return fib.filter(isEven).sum
            }
            else { fib = fib ::: List(fib(l-1) + fib(l-2)) }
        }
        return fib.filter(isEven).sum
    }
    def main(args: Array[String]) {
        val n = args(0)
        println(s"\nSum of even-valued fibonacci terms below $n:")
        println(generateFibonacci(n))
    }
}