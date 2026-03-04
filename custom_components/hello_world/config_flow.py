from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "hello_world"

class HelloWorldConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hello World."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # This is where you'd validate a username/password
            return self.async_create_entry(title="Hello World Instance", data=user_input)

        # Show a simple form with one text field
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("username", default="User"): str
            })
        )
