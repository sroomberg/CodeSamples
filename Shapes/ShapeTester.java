import org.junit.*;

public class ShapeTester {
	public static void main(String[] args) {
		// Triangle
		Shape triangle = new Triangle(10,12,5);
		double triangleArea = triangle.getArea();
		double trianglePerimeter = triangle.getPerimeter();
		
		Assert.assertEquals(24.5446,triangleArea,1.0);
		Assert.assertEquals(27.0,trianglePerimeter,1.0);

		System.out.println("Triangle Area: " + triangleArea);
		System.out.println("Triangle Perimeter: " + trianglePerimeter);
		System.out.println();
		// END Triangle
		
		// Circle
		Shape circle = new Circle(5);
		double circleArea = circle.getArea();
		double circlePerim = circle.getPerimeter();
		
		Assert.assertEquals(Math.PI * Math.pow(5,2), circleArea, 1.0);
		Assert.assertEquals(2 * Math.PI * 5, circlePerim, 1.0);
		
		System.out.println("Circle Area: " + circleArea);
		System.out.println("Circle Perimeter: " + circlePerim);
		System.out.println();
		// END Circle
		
		// Rectangle
		Shape rectangle = new Rectangle(5,7);
		double rectangleArea = rectangle.getArea();
		double rectanglePerim = rectangle.getPerimeter();
		
		Assert.assertEquals(35, rectangleArea, 1.0);
		Assert.assertEquals(24, rectanglePerim, 1.0);
		
		System.out.println("Rectangle Area: " + rectangleArea);
		System.out.println("Rectangle Perimeter: " + rectanglePerim);
		System.out.println();
		// END Rectangle
		
		// Ellipse
		Shape ellipse = new Ellipse(10, 5);
		double ellipseArea = ellipse.getArea();
		double ellipsePerim = ellipse.getPerimeter();
		
		Assert.assertEquals(Math.PI * 10 * 5, ellipseArea, 1.0);
		Assert.assertEquals(Math.PI * (45 - Math.sqrt(35 * 25)), ellipsePerim, 1.0);
		
		System.out.println("Ellipse Area: " + ellipseArea);
		System.out.println("Ellipse Perimeter: " + ellipsePerim);
		System.out.println();
		// END Ellipse
		
		// Square
		Shape square = new Square(4);
		double squareArea = square.getArea();
		double squarePerim = square.getPerimeter();
		
		Assert.assertEquals(16,squareArea, 1.0);
		Assert.assertEquals(16, squarePerim, 1.0);
		
		System.out.println("Square Area: " + squareArea);
		System.out.println("Square Perimeter: " + squarePerim);
		System.out.println();
		// END Square
	}
}