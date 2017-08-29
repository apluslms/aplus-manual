package hello

/**
 * This is a very simple stand alone test program to produce feedback sample.
 * In reality, we have used a unit test framework (scalatest) to render
 * student feedback. A set of grading tools could be included in a container
 * so it doesn't have to be repeated for different scala exercises.
 */
object HelloScalaTest {

  def main(args: Array[String]) {

    var points = 0
    var max_points = 4

    try {

	    println("Calling HelloScala.hello method:")
	    val str = HelloScala.hello
	    println(">>> " + str)
	    points += 1

	    if (str == "Hello Scala!") {
	      println("Correct value!")
	      points += 3
	    }
	    else {
	      println("Incorrect value!")
	    }

    } finally {
      println("TotalPoints: " + points)
      println("MaxPoints: " + max_points)
    }
  }
}
