object smallestMultiple {
    def smallestMultiple(n: Int): Int = {
        var smallest = 1
        while(true) {
            var evenMultiple = true
            for(i <- 1 to n + 1) {
                if(smallest % i != 0){ evenMultiple = false }
            }
            if(evenMultiple) { return smallest }
            smallest = smallest + 1
        }
        1 // force compiling
    }
    def main(args: Array[String]) {
        val n = args(0)
        println(s"Smallest positive number that is evenly divisible by all of the numbers from 1 to ${n}:")
        println(smallestMultiple(n.toInt))
    }
}