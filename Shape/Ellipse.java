
public class Ellipse implements Shape {
	
	private double minorAxis, majorAxis;
	
	public Ellipse(double aMinorAxis, double aMajorAxis) {
		this.minorAxis = aMinorAxis;
		this.majorAxis = aMajorAxis;
	}

	@Override
	public double getArea() {
		return Math.PI * this.minorAxis * this.majorAxis;
	}

	@Override
	public double getPerimeter() {
		return Math.PI * ((3 * (this.minorAxis + this.majorAxis)) - 
				Math.sqrt((3 * this.minorAxis + this.majorAxis) * (this.minorAxis + 3 * this.majorAxis)));
	}

}
