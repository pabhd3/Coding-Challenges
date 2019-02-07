object sumSquareDifference {
    def squareSum(n: Int): Int = {
        return List.range(1, n + 1).map(x => x * x).sum
    }
    def sumSquares(n: Int): Int = {
        val sum = List.range(1, n + 1).sum
        return sum * sum
    }
    def main(args: Array[String]) {
        val n = args(0)
        val s1 = squareSum(n.toInt)
        val s2 = sumSquares(n.toInt)
        println(s"Difference between the sum of squares of the first ${n} natural numbers and the square of the sum:")
        println(s"${s2} - ${s1} = ${s2 - s1}")
    }
}