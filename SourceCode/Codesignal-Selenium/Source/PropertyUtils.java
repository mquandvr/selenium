import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Properties;

public class PropertyUtils {

	public static PropertyUtils propUtil = null;
	
	public static Properties property = null;
	
	public static String URL = "./config.properties";

	public PropertyUtils() {
		super();
	}

	public static void loadFile() {
		try(FileReader reader = new FileReader(URL)) {
			property = new Properties();
			property.load(reader);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void writeFile() {
		try(OutputStream output = new FileOutputStream(URL)) {
			property.store(output, null);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static String getValue(String key) {
		Properties prop = property;
		String value = prop.getProperty(key, "");
		return value;
	}
	
	public static void setValue(String key, String value) {
		Properties prop = property;
		prop.setProperty(key, value);
		
		writeFile();
	}
}
