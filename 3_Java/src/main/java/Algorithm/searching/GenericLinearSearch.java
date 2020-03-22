package searching;

public class GenericLinearSearch {
	
	public static <T> int search(T[] array, T key) {
		
		int size = array.length;
		
		for(int i=0; i<size; i++) {
			if(array[i].equals(key)) {
				return i;
			}
		}
		
		return -1;
	}
}
