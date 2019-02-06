object largestPrimeFactor {
    // Determine the factors of int n
    def factors(n: Int): List[Int] = {
        var factors = List(1)
        for(i <- 2 to n) {
            if(n % i == 0) { factors = factors ::: List(i) }
        }
        return factors
    }
    // Determine if int n is prime
    def isPrime(n: Int): Boolean = {
        for(i <- 2 to n - 1) {
            if(n % i == 0) { return false }
        }
        return true
    }
    def main(args: Array[String]) {
        val n = args(0)
        println(s"\nLargest Prime below $n:")
        var largestPrime = 1
        val f = factors(n.toInt)
        println(s"Factors: ${f}")
        f.foreach(i => {
            if(isPrime(i) && i > largestPrime) { largestPrime = i }
        })
        println(s"Largest Prime Factor: ${largestPrime}")
    }
}