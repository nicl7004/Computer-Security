def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
    def loop(acc: A, t: Tree): A = t match {
      case Empty => acc
      case Node(l, d, r) => loop(f(loop(acc,l),d),r)
    }
    loop(z, t)
  }

  // An example use of foldLeft
  def sum(t: Tree): Int = foldLeft(t)(0){ (acc, d) => acc + d }

  // Create a tree from a list. An example use of the
  // List.foldLeft method.
  def treeFromList(l: List[Int]): Tree =
    l.foldLeft(Empty: Tree){ (acc, i) => acc insert i }

def isorder(acc:(Boolean,Option[Int]), d:Int) : (Boolean,Option[Int]) = acc match{
  case (false, _) => (false, None)
  case (_, Some(x)) => if(d>x) (true, Some(d)) else (false, Some(d))
  case(_, None) => (true, Some(d))
}

  def strictlyOrdered(t: Tree): Boolean = {
    val (b, _) = foldLeft(t)((true, None: Option[Int]))(isorder)
      //   /*f(f(z,1),2) where z is true intially*/
      // case ((b, None),i) =>(b,Some(i))
      // case ((b,Some(i)), j) => (b &&(i<j), Some(j))

    b
  }



val tree = treeFromList(List(10,7,9,8));

strictlyOrdered(tree); // true


// ->



// An example use of foldLeft
def sum(t: Tree): Int = foldLeft(t)(0){ (acc, d) => acc + d }

// Create a tree from a list. An example use of the
// List.foldLeft method.
def treeFromList(l: List[Int]): Tree =
  l.foldLeft(Empty: Tree){ (acc, i) => acc insert i }

def strictlyOrdered(t: Tree): Boolean = {
  val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
      def loop(acc: A, t: Tree): A = t match {
        case Empty => acc
        case Node(l, d, r) => loop(f(loop(acc,l),d),r)
      }
      loop(z, t)
    }(t)((true, None: Option[Int])) {
      /*f(f(z,1),2) where z is true intially*/
    case ((b, None),i) =>(b,Some(i))
    case ((b,Some(i)), j) => (b &&(i<j), Some(j))
  }
  b
}

val tree = treeFromList(List(10,7,9,8));

strictlyOrdered(tree); // true

// -->

def treeFromList(l: List[Int]): Tree =
  l.foldLeft(Empty: Tree){ (acc, i) => acc insert i }

def strictlyOrdered(t: Tree): Boolean = {
  val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
      def loop(acc: A, t: Tree): A = t match {
        case Empty => acc
        case Node(l, d, r) => loop(f(loop(acc,l),d),r)
      }
      loop(z, t)
    }(t)((true, None: Option[Int])) {
      /*f(f(z,1),2) where z is true intially*/
    case ((b, None),i) =>(b,Some(i))
    case ((b,Some(i)), j) => (b &&(i<j), Some(j))
  }
  b
}

val tree = treeFromList(List(10,7,9,8));

strictlyOrdered(tree); // true

// -->

def strictlyOrdered(t: Tree): Boolean = {
  val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
      def loop(acc: A, t: Tree): A = t match {
        case Empty => acc
        case Node(l, d, r) => loop(f(loop(acc,l),d),r)
      }
      loop(z, t)
    }(t)((true, None: Option[Int])) {
      /*f(f(z,1),2) where z is true intially*/
    case ((b, None),i) =>(b,Some(i))
    case ((b,Some(i)), j) => (b &&(i<j), Some(j))
  }
  b
}

val tree = def treeFromList(l: List[Int]): Tree =
  l.foldLeft(Empty: Tree){ (acc, i) => acc insert i }(List(10,7,9,8));

strictlyOrdered(tree); // true

// ->


val tree = def treeFromList(l: List[Int]): Tree =
  l.foldLeft(Empty: Tree){ (acc, i) => acc insert i }(List(10,7,9,8));

  def strictlyOrdered(t: Tree): Boolean = {
    val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
        def loop(acc: A, t: Tree): A = t match {
          case Empty => acc
          case Node(l, d, r) => loop(f(loop(acc,l),d),r)
        }
        loop(z, t)
      }(t)((true, None: Option[Int])) {
        /*f(f(z,1),2) where z is true intially*/
      case ((b, None),i) =>(b,Some(i))
      case ((b,Some(i)), j) => (b &&(i<j), Some(j))
    }
    b
  }(tree); // true

// --> *

val tree = Node(Node(Empty,7,Node(Node(Empty,8,Empty),9,Empty)),10,Empty);

  def strictlyOrdered(t: Tree): Boolean = {
    val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
        def loop(acc: A, t: Tree): A = t match {
          case Empty => acc
          case Node(l, d, r) => loop(f(loop(acc,l),d),r)
        }
        loop(z, t)
      }(t)((true, None: Option[Int])) {
        /*f(f(z,1),2) where z is true intially*/
      case ((b, None),i) =>(b,Some(i))
      case ((b,Some(i)), j) => (b &&(i<j), Some(j))
    }
    b
  }(tree); // true


// -> *

  def strictlyOrdered(t: Tree): Boolean = {
    val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
        def loop(acc: A, t: Tree): A = t match {
          case Empty => acc
          case Node(l, d, r) => loop(f(loop(acc,l),d),r)
        }
        loop(z, t)
      }(t)((true, None: Option[Int])) {
        /*f(f(z,1),2) where z is true intially*/
      case ((b, None),i) =>(b,Some(i))
      case ((b,Some(i)), j) => (b &&(i<j), Some(j))
    }
    b
  }(Node(Node(Empty,7,Node(Node(Empty,8,Empty),9,Empty)),10,Empty)); // true

  // ->
  def strictlyOrdered(t: Tree): Boolean = {
    val (b, _) = def foldLeft[A](t: Tree)(z: A)(f: (A, Int) => A): A = {
        def loop(acc: A, t: Tree): A = t match {
          case Empty => acc
          case Node(l, d, r) => loop(f(loop(acc,l),d),r)
        }
        loop(z, t)
      }(Node(Node(Empty,7,Node(Node(Empty,8,Empty),9,Empty)),10,Empty))((true, None: Option[Int])) {
        /*f(f(z,1),2) where z is true intially*/
      case ((b, None),i) =>(b,Some(i))
      case ((b,Some(i)), j) => (b &&(i<j), Some(j))
    }
    b
  }()
