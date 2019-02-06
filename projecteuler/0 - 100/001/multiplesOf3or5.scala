object multiplesOf3or5 {
    def findSum(n: String): Int = {
        // Define the filter used
        def is3or5(i: Int): Boolean = i % 3 == 0 || i % 5 == 0
        // Return the sum of filter applied to list
        return List.range(0, n.toInt).filter(is3or5).sum
    }
    def main(args: Array[String]) {
        val n = args(0)
        println(s"\nSum of multiples of 3 or 5 below $n:")
        println(findSum(n))
    }
}