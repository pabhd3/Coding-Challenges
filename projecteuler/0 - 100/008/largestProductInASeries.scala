object largestProductInASeries {
    def findLargestProduct(choice: String, n: Int, length: Int): (Int, List[String]) = {
        // Declarations
        var series = ""
        var newSeies = List(scala.util.Random.nextInt(10).toString)
        var default = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843
            |8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557
            |6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749
            |3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776
            |6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397
            |5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474
            |8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586
            |1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408
            |0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606
            |0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
            """.stripMargin.replaceAll("\n", "")
        // Make a n-length string of random ints
        if(choice == "n") {
            for(i <- 1 to length - 1) {
                newSeies = newSeies ::: List(scala.util.Random.nextInt(10).toString)
            }
            series = newSeies.mkString("")
        } else {
            series = default
        }
        // Loop through each set of n ints
        println(series)
        var largest = 0
        for(i <- 0 to (length + 1 - n)) {
            val multiples = series.slice(i, i + n)
            if(multiples.length == n) {
                multiples.foreach(print)
                println()
            }
        }
        return (15, List("1", "1", "3", "5"))
    }
    def main(args: Array[String]) {
        var length = 0
        // Get Parameters from passed args
        val choice = args(0)
        val n = args(1)
        val l = args(2)
        if(choice == "y") {
            length = 1000
        } else {
            length = l.toInt
        }
        println(findLargestProduct(choice, n.toInt, length))
    }
}