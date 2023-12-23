package pageObjectModel;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class SauceCheckoutPage {
    WebDriver Sdriver=null;
    public SauceCheckoutPage(WebDriver driver){
        Sdriver = driver;
        PageFactory.initElements(Sdriver, this);
    }
    @FindBy(xpath = "//button[@id='checkout']")
    private WebElement checkOut;
    public WebElement getCheckOut(){
        return checkOut;
    }
    @FindBy (xpath = "//input[@id='first-name']")
    private WebElement firstname;
    public WebElement getFirstname(){
        return firstname;
    }

    @FindBy (xpath = "//input[@id='last-name']")
    private WebElement lastname;
    public WebElement getLastname(){
        return lastname;
    }
    @FindBy (xpath = "//input[@id='postal-code']")
    private WebElement postalCode;
    public WebElement getPostalCode(){
        return postalCode;
    }

    @FindBy (xpath = "//input[@id='continue']")
    private WebElement continueBtn;
    public WebElement getContinueBtn() {
        return continueBtn;
    }
    @FindBy (xpath = "//button[@id='finish']")
    private WebElement finishBtn;

    public WebElement getFinishBtn(){
        return finishBtn;
    }
    @FindBy (xpath = "//h2[contains(text(),'Thank you for your order!')]")
    private WebElement finishPageHeader;

    public WebElement getFinishPageHeader(){
        return finishPageHeader;
    }
}
