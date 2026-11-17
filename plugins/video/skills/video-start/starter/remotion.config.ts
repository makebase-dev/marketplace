import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
// If Remotion cannot download its browser, point it at an installed one:
// Config.setBrowserExecutable("/path/to/chrome");
