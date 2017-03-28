
public class Circle implements Shape {
	
	private int radius;
	
	public Circle(int aRadius) {
		this.radius = aRadius;
	}

	@Override
	public double getArea() {
		return Math.PI * Math.pow(this.radius,2);
	}

	@Override
	public double getPerimeter() {
		return 2 * Math.PI * this.radius;
	}

}
