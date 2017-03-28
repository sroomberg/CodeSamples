
public class Square implements Shape {
	
	private double side;
	
	public Square(double aSide) {
		this.side = aSide;
	}

	@Override
	public double getArea() {
		return Math.pow(this.side,2);
	}

	@Override
	public double getPerimeter() {
		return 4 * this.side;
	}

}
