const defaultTheme = require('tailwindcss/defaultTheme');
const colors = require('tailwindcss/colors');

module.exports = {
	content: ["./encuestas/templates/**/*.html"],
	theme: {
		extend: {},
	},
	plugins: [require('@tailwindcss/forms')],
};
