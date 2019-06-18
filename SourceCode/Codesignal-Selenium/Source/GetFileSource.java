import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class GetFileSource {

	public static void main(String[] args) {
		ArrayList<String> urlList = new ArrayList<>();
		PropertyUtils.loadFile();
		// declaration and instantiation of objects/variables
		// System.setProperty("webdriver.chrome.marionette","E:\\chromedriver.exe");
		System.setProperty("webdriver.chrome.driver", PropertyUtils.getValue(Constants.PROPERTY_CHOMEDRIVE));

		int count = Integer.parseInt(PropertyUtils.getValue(Constants.PROPERTY_CRAW_PAGE));
		while (count < 1000) {
			WebDriver driver = new ChromeDriver();
			System.out.println("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Tao file Page : " + count);
			Login(driver);
			CodeFight(driver, urlList, count);
			count++;
			PropertyUtils.setValue(Constants.PROPERTY_CRAW_PAGE, String.valueOf(count));
			driver.close();
		}
	}

	@SuppressWarnings("static-access")
	public static Integer CodeFight(WebDriver driver, ArrayList<String> urlList, int page) {
		Integer sleep = 10;
		String baseUrl = "https://app.codesignal.com/tournaments/page/" + String.valueOf(page);

		try {
			/// vao tour
			driver.get(baseUrl);
			Thread.currentThread().sleep(5000);

			WebElement table = driver.findElement(By.tagName("tbody"));
			List<WebElement> rows = table.findElements(By.tagName("tr"));
			List<String> urlLst = new ArrayList<>();
			for (WebElement webElement : rows) {
				String url = webElement.findElement(By.tagName("a")).getAttribute("href");
				urlLst.add(url);
			}
			
			if(page == 1) {
				urlLst.remove(0);
			}

			for (String string : urlLst) {
				String urlA = string.concat("/A");
				String urlB = string.concat("/B");
				String urlC = string.concat("/C");
				String urlD = string.concat("/D");
				String urlE = string.concat("/E");
				LoopAB(driver, urlA);
				LoopAB(driver, urlB);
				LoopAB(driver, urlC);
				LoopAB(driver, urlD);
				LoopAB(driver, urlE);

			}

		} catch (Exception ex) {
			System.out.println(ex.getMessage());
		} finally {

		}
		return sleep;
	}

	@SuppressWarnings("static-access")
	public static void LoopAB(WebDriver driver, String url) {

		try {
			driver.get(url);

			Thread.currentThread().sleep(5000);
			String language = "";

			WebElement solution = driver.findElement(By.cssSelector("div:nth-child(2) > .vertical-tabs--item"));

			solution.click();
			Thread.currentThread().sleep(5000);

			List<WebElement> solutionRows = driver.findElements(By.cssSelector(".rt-tr-group"));
			Thread.currentThread().sleep(2000);
			for (WebElement detailSolutionRows : solutionRows) {
				List<WebElement> detailSolution = detailSolutionRows.findElements(By.cssSelector(".rt-td"));
				if (language.length() == 0 && (detailSolution.get(2).getText().contains("Py3"))) {
					language = detailSolution.get(2).getText();
					detailSolution.get(2).click();
					Thread.currentThread().sleep(2000);
					break;
				}
			}
			if (language.length() > 0) {
				Thread.currentThread().sleep(2000);
				WriteFile(driver, language);
			}

		} catch (Exception e) {
			// see task
			 System.out.println("REGISTER Khong tim thay");
		}

	}

	@SuppressWarnings("static-access")
	public static void Login(WebDriver driver) {

		String loginUrl = "https://app.codesignal.com/login";

		try {
			driver.get(loginUrl);
			Thread.currentThread().sleep(2000);
			driver.findElement(By.name("username")).sendKeys("mquandvr_fjs");
			driver.findElement(By.name("password")).sendKeys("Abc12345@");
			Thread.currentThread().sleep(2000);
			driver.findElement(By.cssSelector(".-padding-v-2 > .button--content")).click();
			;
			System.out.println("Login OK");
			Thread.currentThread().sleep(2000);

		} catch (Exception ex) {
			System.out.println(ex.getMessage());
		} finally {

		}
	}

	@SuppressWarnings("static-access")
	private static boolean WriteFile(WebDriver driver, String language) {
		String methodName = "";
		try {
			WebElement code = driver.findElement(By.cssSelector(".CodeMirror textarea"));
			;
			// WebElement code = driver.findElement(By.className("CodeMirror-code"));;
			// JavascriptExecutor js = (JavascriptExecutor) driver;

			WebElement menthodNameElement = driver.findElement(By.cssSelector(".cm-def:nth-child(2)"));

			methodName = menthodNameElement.getText();
			if (methodName.length() > 0) {
				// menthodName = menthodName.split("(")[0];
				// menthodName = menthodName.replace("function ", "");
//			     String folderJS ="E:\\share$\\Presentation\\Selenium\\SourceCode\\Codesignal-Selenium\\SourceNew\\JS\\";
//			     String folderJava = "E:\\share$\\Presentation\\Selenium\\SourceCode\\Codesignal-Selenium\\SourceNew\\Java\\";
				String folderPy = "E:\\share$\\Presentation\\Selenium\\SourceCode\\Codesignal-Selenium\\SourceNew\\Py3\\";

				String folder = "";
				String content = "";

				code.sendKeys(Keys.CONTROL + "a");
				Thread.currentThread().sleep(2000);
				code.sendKeys(Keys.CONTROL + "c");

				content = (String) Toolkit.getDefaultToolkit().getSystemClipboard().getData(DataFlavor.stringFlavor);
				Thread.currentThread().sleep(1000);
//				if(language.equals("JS")) {
//					folder = folderJS;
//				}
//				if(language.equals("Java")) {
//					folder = folderJava;
//				}
				if (language.equals("Py3")) {
					folder = folderPy;
					createFileSource(folder, methodName, language, content);
				}

			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {

		}
		return true;
	}

	private static void createFileSource(String folder, String fileName, String extention, String content)
			throws IOException {
		File file = new File(folder + fileName + "." + extention.toLowerCase());
		// Create the file
		if (file.createNewFile()) {
			System.out.println("File is created!" + file.getName());
		} else {
			System.out.println("File already exists." + file.getName());
		}

		// Write Content
		FileWriter writer = new FileWriter(file);
		writer.write(content);
		writer.close();
	}
}
