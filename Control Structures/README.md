# Control Structures Code

### Dependencies: Java 1.8
### Compile: javac -cp . Collections.java
### Run: java -cp . Collections

This code is a sample written to optimize a code snippet of several for-loops to use a single control structure and also to improve upon the snippet to make it work up to the <em>n<sup>th</sup></em> number rather than the hard-coded 5 in the example.

<code>
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
</code>