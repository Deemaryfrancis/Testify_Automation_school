package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class Task12 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url - draggable
        driver.get("https://jqueryui.com/");
        Thread.sleep(1000);
        driver.findElement(By.xpath("//a[contains(text(),'Resizable')]")).click();
        Thread.sleep(1000);
        WebElement iframe = driver.findElement(By.xpath("//body/div[@id='container']/div[@id='content-wrapper']/div[1]/div[1]/iframe[1]"));
        driver.switchTo().frame(iframe);
        WebElement resize =  driver.findElement(By.id("resizable"));

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].style.width = '350px';", resize); // Set new width
        js.executeScript("arguments[0].style.height = '350px';", resize);
        Thread.sleep(3000);

        driver.close();
    }
}