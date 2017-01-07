
public class Triangle implements Shape {

	private double side0, side1, side2;

	public Triangle(int aSide0, int aSide1, int aSide2) {
		this.side0 = aSide0;
		this.side1 = aSide1;
		this.side2 = aSide2;
	}

	@Override
	public double getArea() {
		double s = this.getPerimeter() / 2;

		if (this.side0 <= this.side1 && this.side0 <= this.side2) {
			double h = 2 / this.side0 * Math.sqrt(s * (s - this.side0) * (s - this.side1) * (s - this.side2));
			return (0.5 * this.side0 * h);
		}
		else if (this.side1 <= this.side0 && this.side1 <= this.side2) {
			double h = 2 / this.side1 * Math.sqrt(s * (s - this.side0) * (s - this.side1) * (s - this.side2));
			return (0.5 * this.side1 * h);
		}
		else if (this.side2 <= this.side0 && this.side2 <= this.side1) {
			double h = 2 / this.side2 * Math.sqrt(s * (s - this.side0) * (s - this.side1) * (s - this.side2));
			return (0.5 * this.side2 * h);
		}
		return -1.0;
	}

	@Override
	public double getPerimeter() {
		return (this.side0 + this.side1 + this.side2);
	}
}