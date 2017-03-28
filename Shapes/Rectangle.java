
public class Rectangle implements Shape {
	
	private double sideA, sideB;
	
	public Rectangle(double aSideA, double aSideB) {
		this.sideA = aSideA;
		this.sideB = aSideB;
	}

	@Override
	public double getArea() {
		return this.sideA * this.sideB;
	}

	@Override
	public double getPerimeter() {
		return (2 * this.sideA) + (2 * this.sideB);
	}

}
