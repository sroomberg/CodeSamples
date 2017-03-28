import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class Collections {
	
	public static void shuffle(int[] aList) {
		Random rand = ThreadLocalRandom.current();
		for (int i = aList.length - 1; i > 0; i--) {
			int j = rand.nextInt(i + 1);
			int temp = aList[j];
			aList[j] = aList[i];
			aList[i] = temp;
		}
	}

	public static int[] combine(int[] a1, int[] a2) {
		Hashtable<Integer,Integer> freqs = new Hashtable<Integer,Integer>();

		for (int i: a1) {
			if (freqs.containsKey(i)) {
				freqs.put(i, freqs.get(i) + 1);
			}
			else {
				freqs.put(i, 1);
			}
		}
		for (int i: a2) {
			if (freqs.containsKey(i)) {
				freqs.put(i, freqs.get(i) + 1);
			}
			else {
				freqs.put(i, 1);
			}
		}

		int[] ret = new int[freqs.size()];
		int index = 0;
		for (int key: freqs.keySet()) {
			ret[index++] = key;
		}
		Arrays.sort(ret);

		return ret;
	}

	public static void addKeyValuePair(Hashtable<String,Integer> ht, String key, int value) {
		if (ht.containsKey(key)) {
			System.out.println("CANNOT ADD, ALREADY EXISTS: Key = " + key + " | Value = " + value);
		}
		else {
			ht.put(key,value);
		}
	}

	public static void main(String[] args) {
		int[] r1 = {1,2,3,4,5,6,7,8,9,10};
		int[] r2 = {6,7,8,9,10,11,12,13,14,15};

		System.out.println("Collections before modifications:");
		System.out.print("\tr1 = {");
		for (int i: r1) {
			System.out.print(" " + i + " ");
		}
		System.out.println("}");
		System.out.print("\tr2 = {");
		for (int i: r2) {
			System.out.print(" " + i + " ");
		}
		System.out.println("}");
		System.out.println();

		// shuffle arrays
		shuffle(r1);
		shuffle(r2);

		System.out.println("Collections after shuffling:");
		System.out.print("\tr1 = {");
		for (int i: r1) {
			System.out.print(" " + i + " ");
		}
		System.out.println("} | Size of r1 = " + r1.length);
		System.out.print("\tr2 = {");
		for (int i: r2) {
			System.out.print(" " + i + " ");
		}
		System.out.println("} | Size of r2 = " + r2.length);
		System.out.println();

		// combine arrays without duplicates
		int[] c = combine(r1,r2);

		// remove middle entry
		c[c.length / 2] = -1;
		int[] c1 = new int[c.length - 1];
		int c1Index = 0;
		for (int i: c) {
			if (i == -1) {
				continue;
			}
			c1[c1Index++] = i;
		}

		// print c1 in reverse order
		System.out.println("c1 in reverse order");
		System.out.print("\t{");
		for (int i = c1.length - 1; i >= 0; i--) {
			System.out.print(" " + c1[i] + " ");
		}
		System.out.println("} | Size of c1 = " + c1.length);
		System.out.println();

		// key/value pair collection
		Hashtable<String,Integer> ht = new Hashtable<String,Integer>();
		addKeyValuePair(ht, "A", 1);
		addKeyValuePair(ht, "B", 2);
		addKeyValuePair(ht, "C", 3);
		addKeyValuePair(ht, "Z", 26);
		addKeyValuePair(ht, "E", 5);
		addKeyValuePair(ht, "Z", 26);

		System.out.println("Key/Value Pair collection: " + ht.toString());
		System.out.println("Size of Key/Value Pair collection = " + ht.size());
		// I chose to use a hashtable for the key/value pair collection as
		// hashtables are pre-optimized for any type value mapped to any type key.

		
	}


}