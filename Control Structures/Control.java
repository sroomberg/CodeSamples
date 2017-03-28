/*
Given the following lines of code:

for (int i = 1; i <= 5; i++) {
	for (int j = 1; j <= (5 - i); j++) {
		System.out.print(".");
	}
	for (int k = 1; k <= i; k++) {
		System.out.print(i);
	}
	System.out.println();
}

Output:

....1
...22
..333
.4444
55555

Rewrite the code to only use 1 control structure (You can use any Java built-in library you want).
How would you rewrite this for the nth number instead of ending at 5?
*/

public class Control {

	public static void loop(int limit) {	// rewritten to work with only one control structure to the nth limit
		int i = 1, j = 0, n = limit;
		while (i <= n) {
			if (n == i) {
				System.out.print(i);
			}
			else {
				if (j + i >= n) {
					System.out.print(i);
				}
				else {
					System.out.print(".");
				}
			}
			j++;

			if (j == n) {
				j = 0;
				i++;
				System.out.println();
			}
		}
	}

	public static void basicLoop() { // rewritten with only one control structure
		int i = 1, j = 0, n = 5;
		while (i <= n) {
			if (n == i) {
				System.out.print(i);
			}
			else {
				if (j + i >= n) {
					System.out.print(i);
				}
				else {
					System.out.print(".");
				}
			}
			j++;

			if (j == n) {
				j = 0;
				i++;
				System.out.println();
			}
		}
	}

	public static void main(String[] args) {
		basicLoop();
		System.out.println();
		loop(7);
	}

}