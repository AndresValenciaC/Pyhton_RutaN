<div align="center">
  <img src="https://i.postimg.cc/FFSRDrCJ/Imagen3.jpg" alt="Imagen3.jpg">
</div>


## Introduction


Welcome to an extraordinary journey into the realms of space exploration! Our project, in collaboration with Softserve, delves into the vast mysteries of the cosmos, pushing the boundaries of human knowledge and technology.

In the pursuit of unraveling the secrets of the universe, we specialize in the generation of advanced simulations and the creation of comprehensive mission reports for space exploration endeavors. These simulations, powered by cutting-edge technology, replicate various aspects of space missions, allowing us to analyze and anticipate challenges that astronauts and spacecraft may encounter.

### Table of Contents

- [Installation](#installation)
- [Configurations](#configurations)
- [Testing](#testing)
- [Next Steps](#next-steps)
- [Contributions](#contributions)
- [Roadmap](#roadmap)
- [Creators](#creators)
- [Sponsors](#sponsors)
- [License](#license)
- [Thanks](#thanks)

## Installation

Clone the project

```bash
  git clone https://github.com/AndresValenciaC/Pyhton_RutaN.git
```

Go to the project directory

```bash
  cd Pyhton_RutaN
```

Install dependencies

```bash
  poetry install
```

Activate the virtual environment

```bash
  poetry shell
```

Run the program

```bash
  python main.py
```

## Configurations

You can customize the configuration settings in two ways:

### Option 1: Modify `config.yaml`

1. Open the `config.yaml` file located in the project's root directory.

2. Locate the relevant configuration section you want to modify, which may include `numfiles_initicial`, `numfiles_final`, `time_cycle`, `status`, `missions`, `devices`, `date_format`, and others.

3. Update the necessary parameters according to your requirements.

4. Save the changes to the `config.yaml` file.

### Option 2: Use argparse

Alternatively, you can change specific configurations using command-line arguments with argparse. Here are the variables you can use:

- `--numfiles_initial`: Specify the initial number of files.
- `--numfiles_final`: Specify the final number of files.
- `--time_cycle`: Specify the time cycle.

Example:

```bash
python main.py --num_files_initial 5 --num_files_final 24 --time_cycle 8
```
## Testing

To ensure the reliability and quality of the project, thorough unit testing is employed. Here are the key unit test files:

[Files Generation](/tests/test_files_generation.py)  
[Reports](/tests/test_reports_file.py)  
[Backup](/tests/test_backup_file.py)  


These unit tests validate individual components and functions, ensuring they perform as expected. The test suite achieves a test coverage of over 60%, demonstrating a comprehensive examination of the codebase.

For more details on running these tests locally or contributing to the testing process, refer to the [Contributions](#contributions) section.

## Next Steps

The project is currently in its early stages, focusing on fundamental functionality through the command line interface. As it evolves, there are plans to introduce a user interface to enhance the overall user experience.

### Current Phase

In its current phase, the project has established essential functionality accessible through command-line operations.

### Upcoming Enhancements

As part of the next steps, the intention is to implement a graphical user interface, providing a more intuitive and user-friendly experience. This will enable a simpler and visually engaging interaction with the project's features.

## Contributions

Community contributions are encouraged to enhance and expand the project. Whether you have ideas, suggestions, or a desire to participate in development, your involvement is welcome!.

> **Note:**
> This project is in a continuous state of evolution, with upcoming enhancements dedicated to providing a more comprehensive and user-friendly experience.


Thank you for your interest and collaboration in advancing this project.

## Roadmap

### Version 1.1 (Next Release)

- [ ] Implement feature A to enhance functionality.
- [ ] Address user-reported bugs and issues.
- [ ] Optimize codebase for improved performance.

### Version 1.2

- [ ] Introduce a user-friendly graphical user interface (GUI).
- [ ] Add support for multiple languages.
- [ ] Enhance documentation with more detailed usage examples.

### Version 2.0 (Major Update)

- [ ] Integrate advanced analytics and reporting features.
- [ ] Explore compatibility with additional platforms.
- [ ] Conduct usability testing for further improvements.

### Future Considerations

- [ ] Explore potential integrations with third-party services.
- [ ] Enhance accessibility features for a broader user base.
- [ ] Gather user feedback for continuous improvement.

Feel free to contribute to discussions and provide feedback on the Feedback section to influence the roadmap!


## Creators

Feel free to reach out to us if you have any questions or feedback. We value your input! Here are the channels for contacting the creators:


[Andrés Valencia](https://www.linkedin.com/in/juan-felipe-prada-suarez/)  
[ Juan Felipe Prada ](https://www.linkedin.com/in/juan-felipe-prada-suarez/)  
[Miguel Angel Mulcue](https://www.linkedin.com/in/miguel-mulcue/)  



## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.

<div style="text-align: center; line-height: 50px;">
  <a href="https://www.softserveinc.com/en-us" target="_blank" style="vertical-align: middle;">
    <img src="https://cdn.uc.assets.prezly.com/ddf4c03a-d313-4c22-a66a-4f9da1c6939e/" style="width: 50px; height: 100%; vertical-align: middle;">
  </a>
  <a href="https://www.rutanmedellin.org/" target="_blank" style="vertical-align: middle;">
    <img src="https://info.rutanmedellin.org/hubfs/Landing%20ruta%20n/VentaEspacios/thumbnail_pagina.png" style="width: 50px; height: 100%; vertical-align: middle;">
  </a>
</div>


## License

This Proyect is [licensed](./LICENSE).

This Proyect documentation (e.g., `.md` files in the `/docs` folder) is [Team 32 licensed](./LICENSE-docs).

## Thanks

[Luis Vásquez - Teacher](https://www.linkedin.com/in/luisvasv/)

[Sebástian Eusse - Monitor](https://www.linkedin.com/in/sebastian-eusse/)

[CodingUpMyFuture - Bootcamp](https://github.com/codingupmyfuture)