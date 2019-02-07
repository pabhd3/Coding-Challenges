object nthPrime {
    // Determine if int n is prime
    def isPrime(n: Int): Boolean = {
        for(i <- 2 to n - 1) {
            if(n % i == 0) { return false }
        }
        return true
    }
    def findNthPrime(n: Int): Int = {
        var i = 2
        var count = 0
        while(true) {
            if(isPrime(i)) {
                count = count + 1
                if(count == n) { return i }
            }
            i = i + 1
        }
        0 // force compile
    }
    def main(args: Array[String]) {
        val n = args(0)
        println(s"The ${n}  th prime is:")
        println(findNthPrime(n.toInt))
    }
}