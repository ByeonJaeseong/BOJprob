import java.util.LinkedList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		List<String> list = new LinkedList<String>();
		for(int i=1;i<=10000;i++) {
			list.add(String.valueOf(i));
		}
		for(int i=1;i<=10000;i++) {
			list.remove(String.valueOf(i+i%10+((i/10)%10)+((i/100)%10)+((i/1000)%10)+((i/10000)%10)));
			/*System.out.println(String.valueOf(i+i%10+((i/10)%10)+((i/100)%10)+((i/1000)%10)+((i/10000)%10)));*/
		}
		for(int i=0;i<list.size();i++) {
			System.out.println(list.get(i));
		}

	}

}